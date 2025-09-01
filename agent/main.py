from questioner.questioner import build_agent_with_mcp_tools
from dotenv import load_dotenv
import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

# Example usage for testing
if __name__ == "__main__":
    import os

    async def main():
        # You can set your OpenAI API key here or use environment variable
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

        agent = await build_agent_with_mcp_tools(
            model_name="gpt-5",
            temperature=0.01,
            timeout=60,
            api_key=api_key,
            tools=tools,
        )
        # Example: ask the agent a question
        result = await agent.ainvoke(
            {"messages": "Tell me a random joke and a cat fact."}
        )
        print(result)

    asyncio.run(main())
