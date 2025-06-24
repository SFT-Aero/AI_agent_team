# Agent to challenges choices and identify possible flaws/biases

from crewai import Agent, Task
from llm import llm

critique_agent = Agent(
    role="Critical Evaluator",
    goal="Challenge assumptions, detect flaws, and identify possible biases in articles, ideas, or analyses to improve decision quality.",
    verbose=True,
    llm=llm,
    backstory=(
        "You are a critical thinker trained in logical reasoning, cognitive biases, and adversarial evaluation. "
        "Your role is to constructively challenge content by finding logical flaws, unsupported assumptions, and potential biases. "
        "You help ensure insights are robust, balanced, and consider multiple perspectives."
    ),
    allow_delegation=False
)

critique_task = Task(
    description="""
    Review the provided article analysis or reasoning and critically evaluate it.

    Surface any potential:
    - Logical flaws or inconsistencies
    - Overgeneralizations or unwarranted conclusions
    - Unsupported or weak assumptions
    - Cognitive, cultural, or confirmation biases
    - Missing perspectives or counterarguments

    Ask: What might be incomplete, biased, or overly confident in the reasoning?

    Output a structured dictionary including:
    - A list of potential issues
    - Detected biases
    - Critical questions to deepen analysis and improve robustness
    """,
    input={"signal_analysis": param_data},  
    expected_output="""
    A dictionary structured like:
    {
        "potential_issues": [
            "The conclusion assumes scalability based on a single pilot without adoption data.",
            "Selection bias may be present; only successful cases were reviewed."
        ],
        "bias_detected": [
            "Optimism bias: assumes success without addressing failure risks.",
            "Confirmation bias: focuses on supporting evidence while ignoring counterexamples."
        ],
        "critical_questions": [
            "What alternative explanations might exist for the observed trend?",
            "How robust is the evidence supporting this conclusion?"
        ]
    }
    """,
    max_inter=1,
    tools=[],
    agent=critique_agent
)