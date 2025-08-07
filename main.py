from mcp.server.fastmcp import FastMCP


mcp = FastMCP("my_mcp_server", stateless_http=True, port=8087)


@mcp.tool()
async def magic_number():
    return 27


def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
