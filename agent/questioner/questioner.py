import asyncio

from langgraph.prebuilt import create_react_agent
from model.model import get_model
from dotenv import load_dotenv
import os
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.tools import StructuredTool


class QuestionList(BaseModel):
    questions: List[str] = Field(
        ...,
        description="A list of questions, that can be use to invoke current tool.",
    )


SYSTEM_PROMPT = """You are a query generator.
Return ONLY {"questions": string[] }.
You job is to generate different queries that given toolcall function might be able to handle, don't generate for ask_question_tool function.
"""


def ask_question_tool(query: str) -> str:
    """Echo back the query string."""
    return f"Tool received: {query}"


ask_question = StructuredTool.from_function(
    func=ask_question_tool,
    name="ask_question_tool",
    description="Takes a query string and echoes it back.",
)


async def build_agent_with_mcp_tools(model_name, temperature, timeout, api_key, tools):
    """
    Build a LangGraph agent using MCP tools from a running MCP server.
    """
    llm = get_model(
        model_name=model_name,
        temperature=temperature,
        timeout=timeout,
        api_key=api_key,
    )
    agent = create_react_agent(llm, tools + [ask_question], prompt=SYSTEM_PROMPT)
    return agent
