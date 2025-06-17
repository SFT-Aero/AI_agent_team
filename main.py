from crewai import Crew, Process
from scrapper.webscrapper import scrap
#from agents.researcher_agent import researcher
#from tasks.article_tasks import research_task, evaluate_task, decide_task

import json

# Run your webscraper and get article data
article_data = scrap()  # This should return a list of dicts

# Build and run the Crew
crew = Crew(
    # agents=[researcher, evaluator, consensus],
    # tasks=[research_task(article_data), evaluate_task(), decide_task()],
    # process=Process.sequential
)

crew.kickoff()
