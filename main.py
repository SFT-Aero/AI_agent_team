from crewai import Crew, Process
from scrapper.webscrapper import scrap

from futuristic_agent import futuristic_task, futuristic_agent

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
print(f"Raw Data: {len(raw_data)} articles")

#Step 2: Futuristic agent
futuristic_task = futuristic_task(raw_data)

# Step 3: Run the crew
crew = Crew(
    agents=[futuristic_agent],
    tasks=[futuristic_task]
)

output = crew.kickoff()
print(output)
