from crewai import Agent, Task
from llm import llm

# Creates the LLM-powered futuristic agent
futuristic_agent = Agent(
    role="Foresight Analyst",
    goal="Identify signals of future societal or technological change from real articles",
    backstory="You are an expert at detecting weak signals and early indicators of major future shifts.",
    allow_delegation=False,
    llm=llm
)

# Task for futuristic agent to identify 5 signals given the articles from web scrapper
def futuristic_task(articles):
    # List comprehension to create human-readable summary of all articles
    article_summaries = "\n\n".join([f"Title: {a['title']}\nTeaser: {a['teaser'][:1000]}" for a in articles])  # Limit length

    future_signal_task = Task(
        description=(
            "Analyze the following articles and select the top 5 that represent weak signals or strong indicators "
            "of future change in society, technology, or the environment. Justify each selection briefly."
            f"\n\n{article_summaries}"
        ),
        expected_output="A list of 5 articles with titles and brief justification for why each is a signal of future change.",
        agent=futuristic_agent
    )
    return future_signal_task