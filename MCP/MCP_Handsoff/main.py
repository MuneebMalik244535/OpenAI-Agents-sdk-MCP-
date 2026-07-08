#!/usr/bin/env python
"""MCP Server with Handsoff Tools

This server provides various utility tools for agents to use via the MCP protocol.
It uses FastMCP for simplified server setup with stdio transport.
"""

import sys
import json
import logging
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
# Server name will be "MCP_Handsoff"
mcp = FastMCP("MCP_Handsoff")

# ============ Math Tools ============
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def sub(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers. Returns error message if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ============ String Tools ============
@mcp.tool()
def string_length(text: str) -> int:
    """Get the length of a string."""
    return len(text)

@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

@mcp.tool()
def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

@mcp.tool()
def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

# ============ Data Processing Tools ============
@mcp.tool()
def list_sum(numbers: list) -> int:
    """Sum all numbers in a list."""
    if not numbers:
        return 0
    return sum(numbers)

@mcp.tool()
def list_average(numbers: list) -> float:
    """Calculate average of numbers in a list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

@mcp.tool()
def list_max(numbers: list) -> int | float:
    """Find the maximum value in a list."""
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)

@mcp.tool()
def list_min(numbers: list) -> int | float:
    """Find the minimum value in a list."""
    if not numbers:
        raise ValueError("Cannot find min of empty list")
    return min(numbers)

# ============ Utility Tools ============
@mcp.tool()
def combine_strings(strings: list) -> str:
    """Combine a list of strings into one string."""
    return "".join(strings)

@mcp.tool()
def split_string(text: str, separator: str = " ") -> list:
    """Split a string by a separator."""
    return text.split(separator)

if __name__ == "__main__":
    logger.info("Starting MCP Server: MCP_Handsoff")
    logger.info("Tools available: add, sub, multiply, divide, string_length, reverse_string, to_uppercase, to_lowercase, list_sum, list_average, list_max, list_min, combine_strings, split_string")
    
    # Run with stdio transport (default)
    # This allows the server to communicate via stdin/stdout
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)