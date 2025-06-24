# Agent to picks articles most relevant "signals of change", indicate emerging shifts, weak signals, 
# or early indicators of future transformation in a specific category or domain, within 6 months to 1 or 2 years
# Looks for language or structure that implies shift, disruption, or innovation

from crewai import Agent, Task
from llm import llm
from crewai.tools import RagTool

rag_tool = RagTool()
rag_tool.add(data_type="file", path='/Users/shan/AI_agent_team/scrapper/ws_output.html')

relevance = Agent(
    role="Relevance Analyst",
    goal="To identify and surface content that signals potential future change, regardless of topic or domain, enabling downstream agents to assess novelty and growth potential.",
    verbose = True,
    llm=llm,
    tools=[rag_tool],
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

def create_relevance_task(data):
    relevance_task = Task(
        description="""
        You must analyzing retrived knowledge for explicit indicators of future change.

        Use only the content retrieved by your RagTool - do not hallucinate or add your own assumptions.
        
        Flag content that includes:
            Indicators of disruption, experimentation, or innovation
            First-time occurrences or early adoption patterns
            Shifts in consumer, business, or cultural behavior
            New policies or investments aimed at future goals

        Discard content that is:
            Purely historical or backward-looking
            Descriptive of status quo with no signs of change
            Pass forward only the potentially future-relevant signals for further evaluation.

        You must NOT hallucinate or invent new articles or facts.
        
        If there is no such content, respond: 'None'.

        Output a structured dictionary only summarizing each selected article and its corresponding signal analysis, no extra text..
        """,
        input={"articles": data},
        expected_output="A structured dictionary of future signals or `None'.",
        max_inter=1,
        tools=[],
        agent=relevance
    )
    return relevance_task

"""{
            "title": article,
            "is_relevant": true/false,
            "confidence_score": 0 to 1,
            "reason": "brief explanation based only on the article content",
            "signal_type": "type/category of signal detected in article or 'None'",
            "time_sensitivity": e.g. 'Recent (within 3 months)', 'Not recent',
        }"""