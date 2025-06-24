# Receives and prepares the webscrappers output to be interpreted by agent team
# Makes sure that all downstream agents receive clean, consistent data regardless of source
# This agent will:
    # Standardize categories: ("Tech" → "Technology")
    # Fix dates: parse strings into datetime.date objects or standardized strings
    # Fallbacks: fill missing fields with defaults ('No teaser found')
    # Clean HTML: remove tags from body/teaser fields

from crewai import Agent, Task
from crewai.tools import BaseTool
from bs4 import BeautifulSoup
from llm import llm

import datetime

class ArticleCleaningTool(BaseTool):
    name: str = "Article Cleaning Tool"
    description: str = "Clean raw webscraped article data into standardized JSON format."

    def standardize_category(self, cat):
        category_map = {
            "Tech": "Technology",
            "AI": "Technology",
            "Health": "Health",
            "Science": "Science",
            "Business": "Business",
            "World": "World",
            "International": "World",
            "Books": "Culture",
        }
        if not cat:
            return "Uncategorized"
        return category_map.get(cat.strip(), cat.strip())

    def parse_date(self, date_str):
        try:
            return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date().isoformat()
        except Exception:
            return "Unknown Date"

    def strip_html(self, text):
        return BeautifulSoup(text or "", "html.parser").get_text()

    def clean_articles(self, raw_data):
        cleaned = []
        for article in raw_data:
            cleaned.append({
                "title": article.get("Title", "No title found"),
                "url": article.get("URL", ""),
                "date": self.parse_date(article.get("Date from URL")),
                "category": self.standardize_category(article.get("Category")),
                "teaser": self.strip_html(article.get("Teaser", "No teaser found")),
                "body": self.strip_html(article.get("Body", "No body found")),                
                "image": article.get("Image", ""),
            })
        return cleaned

    def _run(self, inputs: dict) -> dict:
        # Expect input as {"articles": [list_of_article_dicts]}
        articles = inputs.get("articles")
        if not isinstance(articles, list):
            return {"result": "Invalid or missing 'articles' list in input."}

        try:
            cleaned = self.clean_articles(articles)
            return {"result": cleaned}
        except Exception as e:
            return {"result": f"Error during cleaning: {e}"}

# Instantiate your tool
article_cleaning_tool = ArticleCleaningTool()


# Who is doing the job
data_ingestor = Agent(
    role="Data Ingestor",
    goal="Clean, standardize, and prepare raw scraped article data for downstream agents "
        "while strictly avoiding fabrication of any data.",
    verbose=True,
    llm=llm,
    tools=[article_cleaning_tool],
    backstory= "You are a meticulous data specialist who ensures all incoming "
        "webscraped data is accurate, consistent, and easy to process by others. "
        "You clean HTML, normalize categories, parse dates, and fill missing fields only when possible. "
        "You do NOT invent or hallucinate any missing information. "
        "If critical fields like title or body or teaser or url are missing or empty, "
        "denoted by No title, body, teaser, or url found, you remove the entry.",
)

def create_cleaning_task(raw_data):
    # What the job is
    print("Raw data type:", type(raw_data))
    data_ingestor_task = Task(
        description="""
        Clean and structure the raw webscraped news data into 
        structured JSON format with the following fields: title, date, url, category, teaser, body.

        Requirements:
        - Standardize category names (e.g., 'Tech' → 'Technology').
        - Parse and standardize date strings into ISO format (YYYY-MM-DD).
        - Remove any article that lacks essential content (no title or no body).
        - Only use data present in the input; do NOT generate or hallucinate missing information.
        - Output a list of clean, uniform article dictionaries ready for the next processing steps.
        """,
        input={"articles": raw_data},
        expected_output=f'A list of clean, uniform article dictionaries ready for next steps',
        agent=data_ingestor,
        max_inter=3,
    )
    return data_ingestor_task
