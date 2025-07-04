from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="voice_agent",
    model="gemini-2.0-flash-live-001",  # Older 2.0 model supports live audio/video
    description="Agent with voice/video chat capabilties to answer questions using Google Search.",
    # Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search],
)
