from crewai import Crew
from scrapper.webscrapper import scrap, read_urls_from_csv, write_scraped_data_to_csv

from futuristic_agent import futuristic_task, futuristic_agent, disruptive_economy_task

#Step 1: Set up GUI
input_csv = '/Users/shan/AI_agent_team/urls.csv'  # Path to your input CSV with URLs
output_csv = '/Users/shan/AI_agent_team/scraped_articles.csv'  # Path for the output CSV
signals_csv = '/Users/shan/AI_agent_team/all_signals.csv'
econ_csv = '/Users/shan/AI_agent_team/econ_signals.csv'

# Step 1: Read URLs from the input CSV
urls = read_urls_from_csv(input_csv)

# Step 2: Runs the web scraper and gets the article data
raw_data = scrap(urls)
print(f"Raw Data: {len(raw_data)} articles")

# Step 3: Output the scraped data to a new CSV file
write_scraped_data_to_csv(output_csv, raw_data)
print(f"Scraped data has been saved to {output_csv}")

# Step 3: Pass article data to futuristic agent
futuristic_task = futuristic_task(raw_data)
economic_task = disruptive_economy_task(raw_data)

# Step 4: Runs the agent crew
crew = Crew(
    agents=[futuristic_agent],
    tasks=[futuristic_task, economic_task]
)

output = crew.kickoff()
print(output)
