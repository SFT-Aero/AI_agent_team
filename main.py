from crewai import Crew, Process
from scrapper.webscrapper import scrap
from agents.beginning import data_ingester_agent
from agents.beginning.data_ingester_agent import data_ingestor, create_cleaning_task
from agents.parameters import novelty_agent
from agents.parameters.novelty_agent import flag_novelty_task

raw_data = scrap() # Run your webscraper and get article data
data_ingester_task = create_cleaning_task(raw_data)
novelty = flag_novelty_task.a

# Build and run the Crew
crew = Crew(
    agents=[data_ingester_agent, novelty_agent],
    tasks=[data_ingester_task, flag_novelty_task],
    process=Process.sequential
)

crew.kickoff()
