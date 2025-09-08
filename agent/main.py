from questioner.questioner import build_agent_with_mcp_tools
from dotenv import load_dotenv
import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import json

BASE_DIR = os.path.dirname(__file__)


if __name__ == "__main__":
    import os

    async def main():
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        mcp_url = "http://127.0.0.1:8087/mcp"
        client = MultiServerMCPClient(
            {
                "mcp": {
                    "url": mcp_url,
                    "transport": "streamable_http",
                }
            }
        )
        tools = await client.get_tools()
        for current_tool in tools:
            agent = await build_agent_with_mcp_tools(
                model_name="gpt-5",
                temperature=0.01,
                timeout=60,
                api_key=api_key,
                tools=[current_tool],
            )
            result = await agent.ainvoke(
                {
                    "input": "Generate 3 diverse queries to test the given toolcall function."
                }
            )
            assistant_msg = result["messages"][-1]
            questions = json.loads(assistant_msg.content)
            toolcall_questions = {
                "function_name": current_tool.name,
                "questions": questions["questions"],
            }
            print(toolcall_questions)
            file_path = os.path.join(BASE_DIR, "data", "question_list.json")
            with open(file_path, "a", encoding="utf-8") as f:
                json.dump(toolcall_questions, f, indent=4, ensure_ascii=False)
            break

    asyncio.run(main())
