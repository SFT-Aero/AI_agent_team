from crewai import Crew
from scrapper.webscrapper import scrap, read_urls_from_csv, write_scraped_data_to_csv
from futuristic_agent import futuristic_task, futuristic_agent, disruptive_economy_task, parse_agent_output, save_to_csv
from pathlib import Path

home = Path.home()  # This is /Users/yourname
#path = home / 'AI_agent_team' / 'scrapper' / 'ws_output.html'

input_csv = home / 'AI_agent_team' / 'urls.csv'
output_csv = home / 'AI_agent_team' / 'scraped_articles.csv'
signals_csv = home / 'AI_agent_team' / 'general_signals.csv'
econ_csv = home / 'AI_agent_team' / 'economic_signals.csv'

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
disruptive_economy_task = disruptive_economy_task(raw_data)

# Step 4: Runs the agent crew
crew1 = Crew(
    agents=[futuristic_agent],
    tasks=[futuristic_task],
)
#output = crew.kickoff()
futuristic_output = crew1.kickoff()
csv = parse_agent_output(futuristic_output.raw)
save_to_csv(csv, signals_csv)

crew2 = Crew(
    agents=[futuristic_agent],
    tasks=[disruptive_economy_task],
)
economy_output = crew2.kickoff()
csv = parse_agent_output(economy_output.raw)
save_to_csv(csv, econ_csv)

#print(output)

