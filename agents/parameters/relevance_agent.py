# Agent to picks articles most relevant "signals of change", indicate emerging shifts, weak signals, 
# or early indicators of future transformation in a specific category or domain, within 6 months to 1 or 2 years
# Looks for language or structure that implies shift, disruption, or innovation

from crewai import Agent, Task
from llm import llm

relevance = Agent(
    role="Relevance Analyst",
    goal="To analyze the given JSON for potential signals of future change.",
    backstory=(
        "You are a skilled analyst with a background in data interpretation using the given JSON."
        "Your job is to scan broadly across categories and flag content that suggests "
        "something new is beginning, shifting, or evolving."
        "You analyze langauge of transition and analyze the given JSON for future-facing relevance."
    ),
    allow_delegation=False
)

def create_relevance_task(data):
    relevance_task = Task(
        description="""
        Analyze the given JSON and select from the given JSON those that 
        represent signals of potential future change.

        Select from the given JSON content that includes:
        -Indicators of disruption, experimentation, or innovation
        -First-time occurrences or early adoption patterns
        -Shifts in consumer, business, or cultural behavior
        -New policies or investments aimed at future goals

        Output a structured dictionary summarizing each selected article 
        only from the given JSON and its corresponding signal analysis.
        """,
        input={"articles": data},
        expected_output="A dictionary structured like this:"
        """{
            "title: ,
            "URL": ,
            "date": ,
            "category": ,
            "is_relevant": true or false,
            "confidence_score": 0 to 1,
            "reason": ,
        }""",
        max_inter=1,
        tools=[],
        agent=relevance,
        output_file='parameters/relevance.txt'
    )
    return relevance_task