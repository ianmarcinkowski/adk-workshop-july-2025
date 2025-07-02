from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.tools import google_search

GEMINI_MODEL = "gemini-2.5-flash"

# Source: https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/#independent-execution-and-state-management

# Researcher 1: Renewable Energy
researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in energy.
Research the latest advancements in 'renewable energy sources'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    description="Researches renewable energy sources.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="renewable_energy_result",
)

# Researcher 2: Electric Vehicles
researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in transportation.
Research the latest developments in 'electric vehicle technology'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    description="Researches electric vehicle technology.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="ev_technology_result",
)

# Researcher 3: Carbon Capture
researcher_agent_3 = LlmAgent(
    name="CarbonCaptureResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in climate solutions.
Research the current state of 'carbon capture methods'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    description="Researches carbon capture methods.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="carbon_capture_result",
)

# --- 2. Create the ParallelAgent (Runs researchers concurrently) ---
# This agent orchestrates the concurrent execution of the researchers.
# It finishes once all researchers have completed and stored their results in state.
parallel_research_agent = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_agent_1, researcher_agent_2, researcher_agent_3],
    description="Runs multiple research agents in parallel to gather information.",
)

# --- 3. Define the Merger Agent (Runs *after* the parallel agents) ---
# This agent takes the results stored in the session state by the parallel agents
# and synthesizes them into a single, structured response with attributions.
merger_agent = LlmAgent(
    name="SynthesisAgent",
    model=GEMINI_MODEL,  # Or potentially a more powerful model if needed for synthesis
    instruction="""You are a Research Synthesis Specialist. Your role is to create a 
comprehensive, well-structured report by analyzing and synthesizing multiple 
research findings.

## Key Requirements:
1. **Source Fidelity**: Use ONLY the information from the provided summaries 
   below
2. **Attribution**: Clearly indicate which findings come from which research area
3. **Synthesis**: Don't just repeat—analyze connections and present insights 
   coherently
4. **Professional Tone**: Write in a clear, authoritative style suitable for 
   stakeholders

## Research Inputs:
**Renewable Energy Research:**
{renewable_energy_result}

**Electric Vehicle Research:**
{ev_technology_result}

**Carbon Capture Research:**
{carbon_capture_result}

## Required Output Format:

# Sustainable Technology Advancements Report

## Renewable Energy Developments
*Source: Renewable Energy Research*
[Synthesize the renewable energy findings with analysis and context]

## Electric Vehicle Progress
*Source: Electric Vehicle Research*
[Synthesize the EV technology findings with analysis and context]

## Carbon Capture Innovations
*Source: Carbon Capture Research*
[Synthesize the carbon capture findings with analysis and context]

## Strategic Insights
[Identify 2-3 key patterns, trends, or implications that emerge from connecting 
these research areas. Keep this section concise but insightful.]

## Executive Summary
[Provide a compelling 2-3 sentence summary highlighting the most significant 
developments across all three areas.]

Deliver only the formatted report above—no preamble or additional commentary.
""",
    description="Combines research findings from parallel agents into a structured, "
                "cited report, strictly grounded on provided inputs.",
    # No tools needed for merging
    # No output_key needed here, as its direct response is the final output of the sequence
)


# --- 4. Create the SequentialAgent (Orchestrates the overall flow) ---
# This is the main agent that will be run. It first executes the ParallelAgent
# to populate the state, and then executes the MergerAgent to produce the final output.
sequential_pipeline_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    # Run parallel research first, then merge
    sub_agents=[parallel_research_agent, merger_agent],
    description="Coordinates parallel research and synthesizes the results.",
)

root_agent = sequential_pipeline_agent
