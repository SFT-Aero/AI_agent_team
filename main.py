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

# Step 1: Clean raw scraped data
#raw_data = scrap() # Run your webscraper and get article data
#print(f"Raw Data: {len(raw_data)} articles")

dummy_data = [
    {
        "Title": "After lashing out at Israel and Iran, Trump says the 'ceasefire is in effect'",
        "URL": "https://www.npr.org/2025/06/24/nx-s1-5443201/israel-iran-ceasefire-trump",
        "Date from URL": "2025-06-24",
        "Category": "Middle East conflict",
        "Teaser": "President Trump speaks with reporters before boarding Marine One on the South Lawn of the White House, Tuesday.",
        "Body": "Middle East conflictAfter lashing out at Israel and Iran, Trump says the 'ceasefire is in effect'The president said he wasn't happy with Israel after its government said it launched a 'powerful strike' against Iran for allegedly breaking their truce",
        "Image": "https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5365x3017+0+68/resize/300/quality/100/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F13%2Fb5%2F740c29984e5e97306dd189a31e70%2Fap25175399656162.jpg"
    },
    {
        "Title": "Israel strikes Tehran and Fordo site, as Russia backs Iran in deepening conflict",
        "URL": "https://www.npr.org/2025/06/23/nx-s1-5442317/israel-iran-russia-conflict",
        "Date from URL": "2025-06-23",
        "Category": "No category found",
        "Teaser": "No teaser found",
        "Body": "Israel strikes Tehran and Fordo site, as Russia backs Iran in deepening conflict",
        "Image": "No image found"
    }
]

# 1. Clean the data
#cleaning_task = create_cleaning_task(dummy_data)
#crew1 = Crew(
    #agents=[data_loader],
    #tasks=[cleaning_task],
    #process=Process.sequential
#)
#cleaned_data = crew1.kickoff()
#print("Cleaned data object", cleaned_data.tasks_output[0].raw)

# 2. Filter for relevance
relevance_task = create_relevance_task(dummy_data)
crew2 = Crew(
    agents=[relevance],
    tasks=[relevance_task],
    verbose=True,
    process=Process.sequential
)
relevant_data = crew2.kickoff()
print("Relevant data object", relevant_data.tasks_output[0].raw)
