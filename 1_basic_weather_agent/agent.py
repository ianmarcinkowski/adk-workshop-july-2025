from google.adk.agents import Agent
from .tools import get_current_time, get_weather

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    # Instructions to set the agent's behavior.
    instruction=(
        "You are a helpful agent, and part-time pirate who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
