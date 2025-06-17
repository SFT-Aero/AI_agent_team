#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4-1106-preview",
    temperature=0.7,
    openai_api_key=openai_key
)
