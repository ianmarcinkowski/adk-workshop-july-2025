# Google ADK Workshop - July 2025


# Workshop Steps

1.  Environment setup
2.  Run a basic agent using


# Environment Setup

We are assuming you are running on a Linux or MacOS host for these instructions.

## Python setup

We will create a Python virutal environment ([virtualenv Primer](https://realpython.com/python-virtual-environments-a-primer/)) and install Python libraries required for the project.

```bash
python3 -m venv .venv && source ~/.venv/bin/activate
pip install -r requirements.txt
```

## Get an API key for Google's AI Studio

- Navigate to https://aistudio.google.com/apikey and generate a new API key
  - You may need to create a new project 
- Update `multi_tool_agent/.env` with the key you have created

# 1. Run a basic agent

From the Google ADK Quickstart

- `adk run 1_basic_weather_agent`
- Ask the agent for weather in New York
- Ask the agent for weather in another location

