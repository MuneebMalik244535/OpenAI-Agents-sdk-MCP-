# MCP + Agents Integration Setup Guide

## ✅ STATUS: WORKING

Your MCP tools are now successfully integrated with your agents.

## Quick Start (30 seconds)

```bash
cd c:\Users\LENOVO\Desktop\Agents+MCP\OpenAI_Agents_SDK_Practice
python run_agent.py
```

That's it! The agent will:
1. ✓ Start the MCP server automatically
2. ✓ Load all 14 tools
3. ✓ Accept your input
4. ✓ Call tools as needed

## What Changed

**Old approach** (had issues):
- Used `agents` library with MCPServerStdio
- Had Python 3.11 type hint compatibility issues
- Complex JSON-RPC protocol handling

**New approach** (working):
- Uses OpenAI SDK directly
- Manages MCP server via subprocess
- Simpler, more reliable communication
- Automatically handles startup/shutdown

## Example Commands

Once running, try these commands:

### Math Operations
```
"What is 15 + 27?"
"Multiply 12 by 8"
"Divide 100 by 4"
```

### String Operations
```
"Reverse the word 'hello'"
"Convert 'python' to uppercase"
"What's the length of 'MCP Server'?"
```

### Data Processing
```
"Calculate the sum of [10, 20, 30, 40]"
"What's the average of [5, 10, 15, 20]?"
```

### Weather (Local Tool)
```
"What's the weather in New York?"
"Tell me the weather in London"
```

### Combined Requests
```
"Get the weather in Paris, then tell me how many characters are in the city name"
"Calculate the average of [72, 75, 68] and tell me what the uppercase version of 'celsius' is"
```

## File Structure

```
OpenAI_Agents_SDK_Practice/
├── config/
│   └── sdk_client.py           # LLM configuration (Gemini/OpenAI)
├── tools/
│   └── main.py                 # Local tools (weather_tool)
├── worker/
│   └── main.py                 # Main agent that uses MCP
├── .env                        # Environment variables
└── README.md                   # This file
```

## How It Works

1. **Agent Initialization**: Agent is created with:
   - Local tools (weather_tool)
   - MCP server connection
   - LLM model (Gemini)

2. **Tool Discovery**: When agent receives a query:
   - Checks local tools first
   - Checks MCP server for available tools
   - Decides which tools are needed

3. **Tool Execution**:
   - If local tool: executes directly
   - If MCP tool: sends request via Stdio to MCP server
   - Processes result and returns to agent

4. **Response Generation**: Agent uses LLM to generate natural response

## Extending with Custom Tools

### Add Local Tool
Edit `tools/main.py`:
```python
from agents import function_tool

@function_tool
async def my_tool(param: str):
    """Description of tool."""
    return result
```

Then add to agent in `worker/main.py`:
```python
from tools.main import my_tool

# In Agent creation:
tools=[weather_tool, my_tool]
```

### Add MCP Tool
Edit `MCP_Handsoff/main.py`:
```python
@mcp.tool()
def my_mcp_tool(param: str) -> str:
    """Description of tool."""
    return result
```

No additional setup needed - automatically available to agent!

## Troubleshooting

### "MCP Server not found"
- Ensure MCP server is running in separate terminal
- Check the command path is correct

### "Tool not working"
- Verify type hints are correct
- Check function implementation
- Review agent logs for errors

### "Connection timeout"
- MCP server might have crashed
- Restart both server and agent

### API Key Issues
- Verify `.env` file exists
- Check API key is valid
- Ensure key has proper permissions

## Performance Tips

1. **Batch Operations**: Combine multiple requests to reduce overhead
2. **Tool Selection**: Use MCP tools for heavy lifting, local tools for simple operations
3. **Error Handling**: Agent handles MCP failures gracefully

## Next Steps

1. Add more custom MCP tools based on your needs
2. Create specialized agents for different tasks
3. Implement multi-agent communication
4. Add data persistence and caching

For more information, see:
- MCP_Handsoff/README.md
- Agent Architecture documentation
