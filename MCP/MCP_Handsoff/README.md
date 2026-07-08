# MCP Server - Handsoff

This is a Model Context Protocol (MCP) server that provides various tools for agents to use. It's built with FastMCP and can be easily extended with custom tools.

## Available Tools

### Math Operations
- **add(a, b)** - Add two numbers
- **sub(a, b)** - Subtract two numbers
- **multiply(a, b)** - Multiply two numbers
- **divide(a, b)** - Divide two numbers

### String Operations
- **string_length(text)** - Get the length of a string
- **reverse_string(text)** - Reverse a string
- **to_uppercase(text)** - Convert text to uppercase
- **to_lowercase(text)** - Convert text to lowercase

### Data Processing
- **list_sum(numbers)** - Sum all numbers in a list
- **list_average(numbers)** - Calculate the average of numbers in a list

## Running the Server

### Prerequisites
```bash
pip install mcp[cli]
```

### Start the Server
```bash
python main.py
```

The server will start and be ready to receive connections from MCP clients.

## Integration with Agents

The OpenAI Agents SDK can connect to this MCP server using `MCPServerStdio`:

```python
from agents.mcp import MCPServerStdio

mcp_server = MCPServerStdio(
    params={
        "command": "python",
        "args": ["-m", "mcp.cli", "run", "path/to/main.py"]
    }
)
```

Then add it to your agent:

```python
agent = Agent(
    name="Assistant",
    model=llm_model,
    mcp_servers=[mcp_server]
)
```

## Adding Custom Tools

To add a new tool, simply add a function decorated with `@mcp.tool()`:

```python
@mcp.tool()
def my_custom_tool(param1: str, param2: int) -> str:
    """Description of what this tool does."""
    # Implementation
    return result
```

### Type Hints
- Always use type hints for parameters and return values
- Supported types: `str`, `int`, `float`, `bool`, `list`, `dict`
- Add docstrings to describe what the tool does

## Architecture

```
MCP_Handsoff (Server)
    ├── main.py (FastMCP server with tools)
    ├── Tools/
    │   ├── Built-in-tools/ (Core tools)
    │   └── Custom-tools/ (Custom implementations)
    └── README.md
        ↓ (TCP/Stdio Connection)
    OpenAI_Agents_SDK_Practice (Client)
        ├── worker/main.py (Agent that uses MCP)
        ├── tools/main.py (Local tools like weather)
        └── config/sdk_client.py (LLM config)
```

## Communication Flow

1. **Agent needs a tool** → Agent searches available tools
2. **Tool found in MCP** → Agent sends request to MCP server via Stdio
3. **MCP executes tool** → Returns result to agent
4. **Agent processes result** → Incorporates into response

## Troubleshooting

- **Connection fails**: Ensure MCP server is running before starting the agent
- **Tool not found**: Check that the tool is decorated with `@mcp.tool()`
- **Type errors**: Verify parameter types match the function signature
