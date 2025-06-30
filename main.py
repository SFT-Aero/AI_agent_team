from crewai import Crew, Process
from scrapper.webscrapper import scrap

from agents.parameters.relevance_agent import relevance, create_relevance_task

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
print(f"Raw Data: {len(raw_data)} articles")

# Step 3: Run the crew
crew = Crew(
    agents=[future_signal_agent],
    tasks=[future_signal_task]
)

output = crew.kickoff()
print(output)
