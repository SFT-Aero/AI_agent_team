# Agent to determine articles with unique applications or novel ideas

from crewai import Agent, Task
from llm import llm

researcher = Agent(
    role='Senior Researcher',
    goal="""Identify articles presenting truly novel applications or ideas
        that have not been widely considered. Categorize findings into unique applications,
        novel ideas, and innovative approaches, and select the top 1-2 examples
        from each category with clear reasons for their novelty.""",
    verbose=True,
    llm=llm,
    backstory=(
        """Driven by a passion for innovation, you seek out breakthrough research 
        that pushes boundaries and reveals new possibilities. Your expertise lies
        in discerning originality and practical novelty in complex technical literature.""",
    )
)

flag_novelty_task = Task(
    description="""
    Carefully analyze the article's title, abstract, and body to identify
    specific, novel applications or ideas that have not been widely considered or explored before.

    Your goal is to find concrete examples of innovation—unique solutions,
    groundbreaking uses, or original methods that stand out as new in their field.

    Focus on categorizing articles into groups such as:
    - Unique application
    - Novel idea
    - Innovative approach

    From each category, select 1 to 2 articles that best exemplify these qualities.

    For each flagged article, provide:
    - A clear explanation of why it was flagged (what makes the application or idea novel)
    - The category it belongs to

    Output a summary dictionary listing the selected articles per category,
    with their flagged status and reasons.

    Only flag articles that show genuinely new or unexplored applications.
    """,
    expected_output="Dictionary summarizing flagged articles by category, each with reasons for novelty.",
    max_inter=1,
    tools=[],  # no tools, keep it simple
    agent=researcher
)