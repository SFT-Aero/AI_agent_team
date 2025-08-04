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
    article_summaries = "\n\n".join([f"Title: {a['title']}\nTeaser: {a['teaser'][:1000]}" for a in articles])  # Limit length

    future_signal_task = Task(
        description=(
            "Analyze the following articles and select the top 5 that represent weak signals or strong indicators "
            "of future change in society, technology, or the environment. Justify each selection briefly."
            f"\n\n{article_summaries}"
        ),
        expected_output="A list of 5 articles with titles and brief justification for why each is a signal of future change.",
        agent=futuristic_agent
    )
    return future_signal_task

def disruptive_economy_task(articles):
    # List comprehension to create human-readable summary of all articles
    article_summaries = "\n\n".join([f"Title: {a['title']}\nTeaser: {a['teaser'][:1000]}" for a in articles])  # Limit length

    disruptive_signal_task = Task(
        description=(
            "Analyze the articles below and identify the 10 most societally disruptive signals. "
            "Justify each selection briefly."
            "Approach this as a sense-making process: consider systemic shifts, unexpected externalities, behavioral impacts, or technological inflections."
            f"\n\n{article_summaries}"
        ),
        expected_output="A list of 10 articles with titles, 2 sentence summary of the article, and brief justification for why each signal is societally disruptive",
        agent=futuristic_agent
    )
    return disruptive_signal_task

# Tell AI "look at npr and give me the top 10 stories related to AI from date range" show me title, date, first two lines
# Break down how it reduces, deduces, make articles meaningful to use
# How much data, how often do we scrap, do we fact check the data
# Make more of a thought process then just scrapping
# Scrape every 2 days, scrape once a day, Remove articles that are a few months old, want to stay current

def save_signals_to_csv(output_text, output_csv):
    pattern = r"\d+\.\s*Title:\s*(.*?)\nJustification:\s*(.*?)(?=\n\d+\. Title:|\Z)"
    matches = re.findall(pattern, output_text, re.DOTALL)

    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'justification'])
        writer.writeheader()
        for title, justification in matches:
            writer.writerow({'title': title.strip(), 'justification': justification.strip()})