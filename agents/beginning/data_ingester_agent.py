# Receives and prepares the webscrappers output to be interpreted by agent team
# Makes sure that all downstream agents receive clean, consistent data regardless of source
# This agent will:
    # Standardize categories: ("Tech" → "Technology")
    # Fix dates: parse strings into datetime.date objects or standardized strings
    # Fallbacks: fill missing fields with defaults ('No teaser found')
    # Clean HTML: remove tags from body/teaser fields

from crewai import Agent, Task
from llm import llm

import datetime

def standardize_category(cat):
    category_map = {
        "Tech": "Technology",
        "AI": "Technology",
        "Health": "Health",
        "Science": "Science",
        "Business": "Business",
        "World": "World",
        "International": "World",
        'Books': 'Culture',
    }
    if not cat:
        return "Uncategorized"
    return category_map.get(cat.strip(), cat.strip())

def parse_date(date_str):
    try:
        # Try parsing YYYY-MM-DD or similar formats
        return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date().isoformat()
    except Exception:
        return "Unknown Date"

# Who is doing the job
data_ingestor = Agent(
    role="Data Ingestor",
    goal="Clean, standardize, and prepare raw scraped article data for downstream agents",
    verbose=True,
    llm=llm,
    backstory="""You are a meticulous data specialist who ensures all incoming
    webscraped data is accurate, consistent, and easy to process by others.
    You clean HTML, normalize categories, parse dates, and fill missing fields.""",
)

def create_cleaning_task(raw_data):
    # What the job is
    data_ingestor_task = Task(
        description="""Clean HTML tags from teaser and body fields;
            Standardize category names ('Tech' → 'Technology');
            Parse and standardize date strings into ISO format (YYYY-MM-DD);
            Fill missing or empty fields with default placeholder text;
            Output a list of clean, uniform article dictionaries ready for next steps
        """,
        input=raw_data,
        expected_output=f'A list of clean, uniform article dictionaries ready for next steps',
        agent=data_ingestor,
        max_inter=3,
    )
    return data_ingestor_task
