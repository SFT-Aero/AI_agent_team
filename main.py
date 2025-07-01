from crewai import Crew, Process
from scrapper.webscrapper import scrap

from futuristic_agent import futuristic_task, futuristic_agent

# Step 1: Runs the web scraper and gets the article data
raw_data = scrap()
print(f"Raw Data: {len(raw_data)} articles")

#Step 2: Pass article data to futuristic agent
futuristic_task = futuristic_task(raw_data)

# Step 3: Runs the agent crew
crew = Crew(
    agents=[futuristic_agent],
    tasks=[futuristic_task]
)

output = crew.kickoff()
print(output)
