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

def chunk_articles(articles, chunk_size=10):
    for i in range(0, len(articles), chunk_size):
        yield articles[i:i + chunk_size]

# Step 1: Clean raw scraped data
raw_data = scrap() # Run your webscraper and get article data
print(f"Raw Data: {len(raw_data)} articles")

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
all_relevant_outputs = []

for i, batch in enumerate(chunk_articles(raw_data, 10)):
    print(f"\nProcessing relevance batch {i+1} with {len(batch)} articles")
    relevance_task = create_relevance_task(batch)
    crew2 = Crew(
        agents=[relevance],
        tasks=[relevance_task],
        process=Process.sequential
    )
    relevant_data = crew2.kickoff()
    print(f"Batch {i+1} result preview:", relevant_data.tasks_output[0].raw[:500])
    all_relevant_outputs.append(relevant_data.tasks_output[0].raw)