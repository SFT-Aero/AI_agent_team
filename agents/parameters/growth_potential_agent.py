# Agent to judge future growth potential for scale or impact

from crewai import Agent, Task
from llm import llm

growth_judge = Agent(
    role="Strategic Growth Analyst",
    goal="Assess the long-term potential of ideas, projects, or technologies to scale or create significant impact.",
    verbose=True,
    llm=llm,
    backstory=(
        "You are a strategic analyst with deep expertise in forecasting growth potential and evaluating the transformative impact "
        "of innovative efforts. You have experience in venture analysis, technology strategy, and systems thinking. "
        "You assess scalability, addressable market size, adoption feasibility, and the broader systemic influence of emerging ideas. "
        "Your recommendations are forward-looking, grounded in both qualitative insight and practical feasibility."
    ),
    allow_delegation=False
)

growth_potential_task = Task(
    description="""
    Review each input article and evaluate its potential for large-scale impact or growth.

    Consider factors such as:
    - Scalability (Can it be implemented widely or replicated?)
    - Market or adoption potential (Is there a large addressable need or user base?)
    - Systemic impact (Could it shift norms, infrastructure, or behavior at scale?)
    - Feasibility and timing (Is the growth realistic within the next 10, 15, 20 years?)

    For each item, provide:
    - A rating of growth potential: Very High / High / Moderate / Low / Very Low
    - A brief explanation justifying your rating
    - Any recommendations for how it could increase its growth potential

    Output a structured dictionary summarizing each item with its growth rating, explanation, and suggestions.
    """,
    input={cleaned_data},  # or however your data is structured
    expected_output="Dictionary with each item rated and explained in terms of growth potential.",
    max_inter=1,
    tools=[],  # no tools, keep it simple
    agent=growth_judge
)