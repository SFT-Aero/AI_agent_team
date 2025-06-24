from crewai import Crew, Process
from scrapper.webscrapper import scrap
from agents.beginning import data_ingester_agent
from agents.beginning.data_ingester_agent import create_cleaning_task

#from agents.parameters import novelty_agent
#from agents.parameters.novelty_agent import flag_novelty_task

#from agents.parameters import growth_potential_agent
#from agents.parameters.growth_potential_agent import growth_potential_task

from agents.parameters import relevance_agent
from agents.parameters.relevance_agent import create_relevance_task

#from agents.end import critic_agent
#from agents.end.critic_agent import critique_task

#from agents.end import consensus_agent
#from agents.end.consensus_agent import consensus_task

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
print(f"Raw Data: {len(raw_data)} articles")

# 1. Clean the data
cleaning_task = create_cleaning_task(raw_data)
crew1 = Crew(
    agents=[data_ingester_agent],
    tasks=[cleaning_task],
    process=Process.sequential
)
cleaned_data = crew1.run()
print(f"Cleaned Data: {len(cleaned_data)} articles")
print("Cleaned data", cleaned_data)

# 2. Filter for relevance
relevance_task = create_relevance_task(cleaned_output)
crew2 = Crew(
    agents=[relevance_agent],
    tasks=[relevance_task],
    process=Process.sequential
)
relevant_data = crew2.run()
print(f"Relevant Data: {len(relevant_data)} articles")
