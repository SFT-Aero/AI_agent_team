# Agent to picks articles most relevant "signals of change", indicate emerging shifts, weak signals, 
# or early indicators of future transformation in a specific category or domain, within 6 months to 1 or 2 years

from crewai import Agent, Task
from llm import llm

relevance_agent = Agent(
    role="Relevance Analyst",
    goal="Identify articles that act as early signals of change within a topic or domain, based on relevance, recency, and transformative potential.",
    backstory=(
        "You are an expert in foresight analysis, trained to detect early indicators of future change across industries, technologies, and societies. "
        "Your background spans trend analysis, horizon scanning, emerging tech monitoring, and speculative futures research. "
        "You excel at identifying weak signals—subtle but meaningful developments—that may evolve into major shifts. "
        "Your focus is on articles that are not just topically relevant, but that also signal possible transformations in how systems, behaviors, or technologies operate."
    ),
    allow_delegation=False
)

relevance_task = Task(
    description="""
    Review the provided articles and select those that represent **signals of potential future change** within the given category or topic.

    A "signal" might be:
    - A shift in language, values, or approaches that challenge the current norm

    Selection criteria:
    1. **Topical relevance** — The article must relate clearly to the given domain or research question.
    2. **Recency** — Focus on articles published within the last 6 months to 2 years.
    3. **Transformative signal** — The article must indicate a possible future development or emerging pattern.

    For each selected article, provide:
    - A short explanation of the signal and why it matters
    - The type of signal (e.g. Technological, Cultural, Regulatory, Environmental, Market)
    - The publication date
    - A confidence rating (High / Medium / Low) that it reflects meaningful future change

    Output a structured dictionary summarizing each selected article and its corresponding signal analysis.
    """,
    input={"articles": cleaned_data, "topic": topic},  # include 'topic' for context-aware filtering
    expected_output="Dictionary of selected articles with signal type, explanation, date, and confidence level.",
    agent=relevance_agent
)


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