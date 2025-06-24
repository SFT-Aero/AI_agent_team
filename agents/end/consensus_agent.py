# Agent to review all decisions and finalizes the best one per category
# Finalizes the selection
# Writes a 1-2 sentence "why this one" summary
# Provides a confidence level (e.g., based on how unanimous the team was)
# Flags "borderline" picks if necessary

from crewai import Agent, Task
from llm import llm

consensus_agent = Agent(
    role="Decision Finalizer",
    goal=(
        "Review all candidate decisions or selections across categories, "
        "finalize the best choice per category, write a concise rationale, "
        "provide a confidence score based on consensus, and flag borderline picks."
    ),
    verbose=True,
    llm=llm,
    backstory=(
        "You are the final arbiter responsible for synthesizing input from multiple evaluators or agents. "
        "Your expertise lies in weighing evidence, measuring consensus, and making clear, justified final choices. "
        "You help ensure the best, most confident decisions are identified, while transparently flagging uncertain or close calls."
    ),
    allow_delegation=False
)

consensus_task = Task(
    description="""
    Review all candidate selections and evaluations across categories.

    For each category:
    - Select the single best candidate decision or option.
    - Write a 1-2 sentence summary explaining why this choice was selected.
    - Provide a confidence score reflecting the strength of consensus or clarity of choice.
    - Flag the selection as "borderline" if the confidence is low or opinions were divided.

    Output a structured dictionary with category keys, each containing:
    - chosen_item: The selected decision or option
    - rationale: The concise explanation for the choice
    - confidence_score: Float between 0 and 1 indicating confidence level
    - borderline_flag: Boolean indicating if the selection is borderline
    """,
    input={"candidate_evaluations": critic_data},  # e.g. input from multiple evaluators
    expected_output="""
    A dictionary structured like:
    {
        "Category A": {
            "chosen_item": "...",
            "rationale": "...",
            "confidence_score": 0.92,
            "borderline_flag": false
        },
        "Category B": {
            "chosen_item": "...",
            "rationale": "...",
            "confidence_score": 0.65,
            "borderline_flag": true
        }
    }
    """,
    max_inter=1,
    tools=[],
    agent=decision_finalizer_agent
)


