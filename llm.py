from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4-1106-preview",
    temperature=0.2, # Range from 0 to 1: lower temperatures more deterministic, higher temperatures more creative.
    openai_api_key=openai_key
)
