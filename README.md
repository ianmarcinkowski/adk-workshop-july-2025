# Google ADK Workshop - July 2025

# Workshop Steps

1.  Environment setup
2.  Run a basic agent with simple functions as tools
3.  Run an agent with access to a web API
    -  (Optional) Demonstrate Cursor's agent mode to create the API calls for us
4.  Run a workflow agent that demonstrates parallel, sequential workflows

# Environment Setup

We are assuming you are running on a Linux or MacOS host for these instructions.

## Python setup

We will create a Python virutal environment ([virtualenv Primer](https://realpython.com/python-virtual-environments-a-primer/)) and install Python libraries required for the project.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Get an API key for Google's AI Studio

**For the workshop, I will provide an API key to use with your environment to speed up the initial setup**;
however, if you want to go through these examples on your own, follow the `Set up the model` section of 
the ADK Quickstart documentation: https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Here is a basic snippet:

- Navigate to https://aistudio.google.com/apikey and generate a new API key
- Copy `sample.env` to `.env` (To ensure your API key is not commited in Git the `.env` file is ignored by version control)
- Update `.env` with the API key you have created

# 1. Run a basic agent

Source: https://google.github.io/adk-docs/get-started/quickstart/

- `adk run 1_basic_weather_agent`
- Ask the agent for weather in New York
- Ask the agent for weather in another location

# 2. Run agent with access to a public API

Source: https://google.github.io/adk-docs/get-started/quickstart/ with some additions for our workshop

- Open [2_weather_api_agent/agent.py](./2_weather_api_agent/agent.py)
- If using Cursor, delete the implementation of `get_weather_from_api` and ask Agent Mode to update our placeholder function `get_weather_from_api` to call an open weather API. Here is an example prompt that should work reasonably well

  ```
  Let's modify our placeholder function `get_weather_from_api` to call a publicly-accessible weather API.  Please choose an API that does not require an API token.

  Please sanitize the name of the provided city and call a publicly-accessible weather API for the provided location, returning appropriate data to the user.
  ```

- Go through Cursor's Agent Mode prompts as necessary and review the generated code
- Alternatively, if Cursor gets stuck, rename the `PLACEHOLDER_get_weather_from_api` found in [2_weather_api_agent/agent.py](./2_weather_api_agent/agent.py) or update the name of the tool function being passed into our agent
- Run the agent `adk run 2_weather_api_agent`
- Ask for the weather in New York, Toronto, Beijing
- (Optional) Ask Cursor to add a method for fetching time from NIST's time server

#  3. Agent workflows, Parallel and Sequential Agents

Source: https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/#independent-execution-and-state-management

- In your terminal, launch the ADK web UI `adk web`
- Select the `3_workflow_agent` agent from the top-left dropdown
- Search: "Summarize the energy landscape in Canada"

# Sources

- Google ADK Quickstart https://google.github.io/adk-docs/get-started/quickstart
- Workflow Agents https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/#independent-execution-and-state-management
