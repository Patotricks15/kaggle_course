from google.adk.agents.llm_agent import Agent
from sampleagent.config import retry_config
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search

root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)
