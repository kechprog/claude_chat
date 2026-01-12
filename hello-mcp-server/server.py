#!/usr/bin/env python3
"""Simple MCP server with a hello_world endpoint."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world-server")


@mcp.tool()
def hello_world() -> str:
    """Returns a Hello World greeting."""
    return "Hello World"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.sse_app(), host="127.0.0.1", port=8000)
