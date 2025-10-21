"""
Simple MCP server with a greeting tool.

This server provides a single tool that responds to greetings.
Can run in both stdio mode (for local testing) and HTTP mode (for remote access).
"""

import os
from mcp.server.fastmcp import FastMCP

# Create the MCP server with HTTP configuration
mcp = FastMCP(
    "hello-mcp-server",
    host=os.getenv("HOST", "0.0.0.0"),  # Listen on all interfaces in container
    port=int(os.getenv("PORT", "8000"))  # Configurable port
)


@mcp.tool()
def greet(message: str) -> str:
    """
    Respond to a greeting message.
    
    Args:
        message: The greeting message (e.g., "how are you")
    
    Returns:
        A friendly response
    """
    # Check if the message is asking "how are you"
    if "how are you" in message.lower():
        return "I am great"
    
    # Default friendly response for other greetings
    return "Hello! I'm doing well, thanks for asking!"


if __name__ == "__main__":
    # Check transport mode from environment variable
    transport = os.getenv("TRANSPORT", "stdio")
    
    if transport == "http":
        print(f"Starting MCP server on http://{mcp.settings.host}:{mcp.settings.port}/mcp")
        mcp.run(transport="streamable-http")
    else:
        print("Starting MCP server in stdio mode")
        mcp.run(transport="stdio")
