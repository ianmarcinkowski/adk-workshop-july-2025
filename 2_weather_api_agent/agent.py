from google.adk.agents import Agent
from .tools import get_weather_from_api


root_agent = Agent(
    name="weather_api_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about the weather in a city using an open API",
    # Instructions to set the agent's behavior.
    instruction=(
        "You are a helpful agent who can answer user questions about the "
        "weather in a city."
    ),
    tools=[get_weather_from_api],
)
