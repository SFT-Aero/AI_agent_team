from crewai import Crew, Process
from scrapper.webscrapper import scrap
from agents.beginning.data_ingester_agent import data_loader, create_cleaning_task

#from agents.parameters import novelty_agent
#from agents.parameters.novelty_agent import flag_novelty_task

#from agents.parameters import growth_potential_agent
#from agents.parameters.growth_potential_agent import growth_potential_task

from agents.parameters.relevance_agent import relevance, create_relevance_task

#from agents.end import critic_agent
#from agents.end.critic_agent import critique_task

#from agents.end import consensus_agent
#from agents.end.consensus_agent import consensus_task

import re
import datetime

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
print(f"Raw Data: {len(raw_data)} articles")

def parse_article_from_raw_text(raw_text):
    # Extract each field using simple regex
    title_match = re.search(r"Title:\s*(.*)", raw_text)
    url_match = re.search(r"URL:\s*(.*)", raw_text)
    date_match = re.search(r"Date from URL:\s*(.*)", raw_text)
    category_match = re.search(r"Category:\s*(.*)", raw_text)
    teaser_match = re.search(r"Teaser:\s*(.*)", raw_text)
    body_match = re.findall(r"Body:\s*(.*?)Image:", raw_text, re.DOTALL)
    image_match = re.search(r"Image:\s*(.*)", raw_text)

    def parse_date(d):
        try:
            return datetime.datetime.strptime(d.strip(), "%Y-%m-%d").date().isoformat()
        except:
            return "Unknown Date"
        
    return [{
        "title": title_match.group(1).strip() if title_match else "No title found",
        "url": url_match.group(1).strip() if url_match else "",
        "date": parse_date(date_match.group(1)) if date_match else "Unknown Date",
        "category": category_match.group(1).strip() if category_match else "Uncategorized",
        "teaser": teaser_match.group(1).strip() if teaser_match else "No teaser found",
        "body": body_match[0].strip() if body_match else "No body found",
        "image": image_match.group(1).strip() if image_match else "No image found"
    }]


parsed_articles = []
for article_text in raw_data:
    print(type(raw_data))
    parsed = parse_article_from_raw_text(article_text)
    parsed_articles.append(parsed)

print(f"Parsed Data: {len(parsed_articles)} articles")

## 1. Clean the data
#cleaning_task = create_cleaning_task(raw_data)
#crew1 = Crew(
    #agents=[data_loader],
    #tasks=[cleaning_task],
    #process=Process.sequential
#)
#cleaned_data = crew1.kickoff()
#print("Cleaned data object", cleaned_data.tasks_output[0].raw)

# 2. Filter for relevance
relevance_task = create_relevance_task(parsed_articles)
crew2 = Crew(
    agents=[relevance],
    tasks=[relevance_task],
    process=Process.sequential
)
relevant_data = crew2.kickoff()
print(f"Relevant Data: {len(relevant_data)} articles")
