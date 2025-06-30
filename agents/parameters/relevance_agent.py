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
    allow_delegation=False,
    system_template="""
    You are a strict relevance detection agent. You MUST follow these rules:

    - You will ONLY analyze the JSON array of articles given in input.
    - Do NOT generate any new article titles, URLs, dates, categories, teaser text, or body content.
    - Do NOT paraphrase or modify any of the input data fields.
    - You MUST keep the original values EXACTLY as given.
    - The 'reason' field must be a short explanation derived ONLY from the input article's 'teaser' and 'body' fields.
    - If an article lacks sufficient content for relevance judgment, mark "is_relevant": false with an appropriate reason.
    - Output your top 5 most relevant articles.
    - Do NOT hallucinate or fabricate anything.
    """
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

        Use ONLY the data in each article. DO NOT generate or guess missing values (e.g., do not make up new titles, bodies, or links).
        Base your relevance judgment ONLY on the actual text in the 'title', 'teaser', and 'body'.
        If the article lacks content to determine relevance, mark it as not relevant.

        Output your top 5 most relevant articles.
        """,
        input={"articles": data},
        expected_output="Your top 5 most relevent articles and your reason why.",
        max_inter=1,
        tools=[],
        agent=relevance,
        output_file='agents/parameters/relevance.txt'
    )
    return relevance_task