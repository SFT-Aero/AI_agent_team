# Agent to picks articles most relevant "signals of change", indicate emerging shifts, weak signals, 
# or early indicators of future transformation in a specific category or domain, within 6 months to 1 or 2 years
# Looks for language or structure that implies shift, disruption, or innovation

from crewai import Agent, Task
from llm import llm

relevance_agent = Agent(
    role="Relevance Analyst",
    goal="To identify and surface content that signals potential future change, regardless of topic or domain, enabling downstream agents to assess novelty and growth potential.",
    backstory=(
        "You were trained on thousands of weak signals, foresight reports, and innovation briefings. You don’t need a specific topic — "
        "your job is to scan broadly across categories (tech, society, business, culture, science, etc.) "
        "and flag content that suggests something new is beginning, shifting, or evolving. "

        "You’ve been fine-tuned to spot the language of transition — early experiments, "
        "policy changes, cultural shifts, startup launches, prototype testing, emerging needs, "
        "and more. Your job is not to judge how new or scalable the idea is — only whether "
        "it holds future-facing relevance."
    ),
    allow_delegation=False
)

def relevance_task(data):
    relevance_task = Task(
        description="""
        Review the provided articles and select those that represent signals of potential future change.

        Determine if it contains any indication of future 
        change (e.g., new behaviors, technologies, trends, ideas, or systems).

        Flag content that includes:
            Indicators of disruption, experimentation, or innovation
            First-time occurrences or early adoption patterns
            Shifts in consumer, business, or cultural behavior
            New policies or investments aimed at future goals

        Discard content that is:
            Purely historical or backward-looking
            Descriptive of status quo with no signs of change
            Pass forward only the potentially future-relevant signals for further evaluation.

        Output a structured dictionary summarizing each selected article and its corresponding signal analysis.
        """,
        input={"articles": data},
        expected_output="A dictionary structured like this:"
        """{
            "is_relevant": true,
            "confidence_score": 0.87,
            "reason": "The content describes a new city-wide pilot program testing AI-powered traffic signals to reduce urban congestion, which signals experimentation and potential systems-level change.",
            "signal_type": "Technology + Infrastructure",
            "time_sensitivity": "Recent (within 6 months)",
        }""",
        max_inter=1,
        tools=[],
        agent=relevance_agent
    )
    return relevance_task