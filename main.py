from crewai import Crew, Process
from scrapper.webscrapper import scrap
from agents.beginning.data_ingester_agent import data_ingestor, create_cleaning_task
#from agents.researcher_agent import researcher
#from tasks.article_tasks import research_task, evaluate_task, decide_task

import json

raw_data = scrap() # Run your webscraper and get article data
data_ingestor_task = create_cleaning_task(raw_data)

# Build and run the Crew
crew = Crew(
    agents=[data_ingestor],
    tasks=[data_ingestor_task],
    process=Process.sequential
)

crew.kickoff()
