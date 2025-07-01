from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.5-flash",  # Available July 2025
    description="Agent to answer questions using Google Search.",
    # Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search],
)
