from crewai import Agent, Task
from llm import llm
import csv
import re

# Creates the LLM-powered futuristic agent
futuristic_agent = Agent(
    role="Foresight Analyst",
    goal="Identify signals of future societal or technological change from real articles",
    backstory="You are an expert at detecting weak signals and early indicators of major future shifts.",
    allow_delegation=False,
    llm=llm
)

# Task for futuristic agent to identify 5 signals given the articles from web scrapper
def futuristic_task(articles):
    # List comprehension to create human-readable summary of all articles
    article_summaries = "\n\n".join([f"Title: {a['title']}\nURL: {a['url']}\nCategory: {a['category']}\nTeaser: {a['teaser'][:1000]}" for a in articles])  # Limit length

    future_signal_task = Task(
        name="futuristic_task",
        description=(
            "Analyze the following articles and select the top 10 that represent weak signals or strong indicators "
            "of future change in society, technology, or the environment. Justify each selection briefly."
            f"\n\n{article_summaries}"
        ),
        expected_output="A list of 10 articles with titles, urls, categories, 2 sentence summary of the article, and brief justification for why each is a signal of future change.",
        agent=futuristic_agent
    )
    return future_signal_task

def disruptive_economy_task(articles):
    # List comprehension to create human-readable summary of all articles
    article_summaries = "\n\n".join([f"Title: {a['title']}\nURL: {a['url']}\nCategory: {a['category']}\nTeaser: {a['teaser'][:1000]}" for a in articles])  # Limit length

    economic_signal_task = Task(
        description=(
            "Analyze the articles below and identify the 10 most economically disruptive signals. "
            "Justify each selection briefly."
            "Approach this as a sense-making process: consider systemic shifts, unexpected externalities, behavioral impacts, or technological inflections."
            f"\n\n{article_summaries}"
        ),
        expected_output="A list of 10 articles with titles, urls, categories, 2 sentence summary of the article, and brief justification for why each signal is economically disruptive",
        agent=futuristic_agent
    )
    return economic_signal_task

# Tell AI "look at npr and give me the top 10 stories related to AI from date range" show me title, date, first two lines
# Break down how it reduces, deduces, make articles meaningful to use
# How much data, how often do we scrap, do we fact check the data
# Make more of a thought process then just scrapping
# Scrape every 2 days, scrape once a day, Remove articles that are a few months old, want to stay current

def parse_agent_output(agent_output):
    # Split by numbered entries (e.g., 1. Title...)
    entries = re.split(r'\n?\d+\.\s*Title:\s*', agent_output)[1:]  # Skip the first empty match

    parsed_articles = []

    for entry in entries:
        # Clean the entry by removing all unnecessary spaces
        cleaned_entry = re.sub(r'\s+', ' ', entry).strip()  # Replace all excessive whitespaces with a single space
        
        # Split the cleaned entry into lines by detecting "URL:", "Category:", etc.
        title = cleaned_entry.split("URL:")[0].strip()  # Title is before "URL:"
        remaining_text = cleaned_entry.split("URL:")[1].strip()  # Everything after "URL:"
        
        # Use regex to extract URL, Category, Summary, and Justification
        url = re.search(r"URL:\s*(https?://[^\s]+)", remaining_text)
        category = re.search(r"Category:\s*([^\n]+)", remaining_text)
        summary = re.search(r"Summary:\s*([^\n]+)", remaining_text)
        justification = re.search(r"Justification:\s*([^\n]+)", remaining_text)

        # If not found, set default values
        url = url.group(1) if url else "URL Missing"
        category = category.group(1) if category else "Category Missing"
        summary = summary.group(1) if summary else "Summary Missing"
        justification = justification.group(1) if justification else "Justification Missing"

        # Append the parsed data to the list
        parsed_articles.append({
            "Title": title,
            "URL": url,
            "Category": category,
            "Summary": summary,
            "Justification": justification
        })

    return parsed_articles

def save_to_csv(data, filename="future_signals.csv"):
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Category", "Summary", "Justification"])
        writer.writeheader()
        writer.writerows(data)