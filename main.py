from crewai import Crew, Process
from scrapper.webscrapper import scrap
from agents.beginning import data_ingester_agent
from agents.beginning.data_ingester_agent import create_cleaning_task

#from agents.parameters import novelty_agent
#from agents.parameters.novelty_agent import flag_novelty_task

#from agents.parameters import growth_potential_agent
#from agents.parameters.growth_potential_agent import growth_potential_task

from agents.parameters import relevance_agent
from agents.parameters.relevance_agent import relevance_task

#from agents.end import critic_agent
#from agents.end.critic_agent import critique_task

#from agents.end import consensus_agent
#from agents.end.consensus_agent import consensus_task

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
cleaning_task = create_cleaning_task(raw_data) # Assuming this returns list of cleaned articles
cleaned_data = cleaning_task.run()
print(f"Cleaned Data: {len(cleaned_data)} articles")
print("Cleaned data", cleaned_data)

# Step 2: Run Relevance Agent on cleaned data
relevance_task = relevance_task(cleaned_data)  # filtered relevant articles
relevant_data = relevance_task.run()
print(f"Relevant Data: {len(relevant_data)} articles")

# Step 3: Run Novelty Agent on relevant data
#novel_data = flag_novelty_task.run()
#print(f"Novel Data: {len(novel_data)} articles")

# Step 4: Run Growth Potential Agent on relevant data
#growth_data = growth_potential_task.run()
#print(f"Growth Data: {len(growth_data)} articles")


# Build and run the Crew
crew = Crew(
    agents=[data_ingester_agent, relevance_agent],
    tasks=[cleaning_task, relevance_task],
    process=Process.sequential
)

crew.kickoff()
