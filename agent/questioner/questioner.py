import asyncio

from langgraph.prebuilt import create_react_agent
from model.model import get_model
from dotenv import load_dotenv
import os


async def build_agent_with_mcp_tools(
    model_name,
    temperature,
    timeout,
    api_key,
    tools
):
    """
    Build a LangGraph agent using MCP tools from a running MCP server.
    """
    # Get the language model
    llm = get_model(
        model_name=model_name,
        temperature=temperature,
        timeout=timeout,
        api_key=api_key,
    )
    # Create the agent with the model and tools
    agent = create_react_agent(llm, tools)
    return agent
