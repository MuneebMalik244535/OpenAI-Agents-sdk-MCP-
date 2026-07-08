# Problems and Solutions

## 1. Problem: `agents` library import failure
- **Issue:** `worker/main.py` was importing from `agents.mcp` and other `agents` package classes.
- **Observed error:** `KeyError: ~TContext` during import.
- **Cause:** Incompatible `agents` library version with Python 3.11. The repo notes indicate this is a known compatibility issue.

### Solution
- Remove the `agents` library dependency from `worker/main.py`.
- Use the OpenAI SDK directly with `openai.OpenAI` instead of `Agent`, `Runner`, and `MCPServerStdio`.
- Keep the MCP server as a subprocess, not as a direct `agents` MCP connection.
- Use Python 3.12 when possible for the repo’s working solution.

---

## 2. Problem: `worker/main.py` old implementation was broken
- **Issue:** The old worker script relied on `agents` package imports and the local MCP-based agent workflow.
- **Symptom:** The script failed before it could start the agent or connect to tools.
- **Reason:** The code assumed the `agents` SDK import path would work, but the installed package and Python version did not match.

### Solution
- Replace `worker/main.py` with a direct OpenAI SDK-based agent entrypoint.
- Use `client.chat.completions.create(...)` with tool definitions.
- Implement local tool execution logic inside the worker script.
- Start the `MCP_Handsoff/main.py` server via subprocess only for server-side tool availability.

---

## 3. Problem: Tool integration and MCP server connection
- **Issue:** The original flow tried to mix `agents` MCP server integration with local tool definitions.
- **Risk:** If the `agents` library fails, the entire tool workflow breaks.

### Solution
- Keep MCP server startup separate from tool execution logic.
- Define local tool metadata in the agent call so the OpenAI SDK can choose tools.
- Map tool calls returned by the model to Python functions in `worker/main.py`.
- Example tools added: `add`, `multiply`, `divide`, `reverse_string`, `to_uppercase`, `weather_tool`.

---

## 4. Problem: Python version mismatch
- **Issue:** Python 3.11 was installed, but the repo and docs reference Python 3.12 as more reliable.
- **Evidence:** `Improvements/README.md`, `INTEGRATION_GUIDE.md`, and `README_WORKING_SOLUTION.md` all mention Python 3.12 and compatibility issues with `agents`.

### Solution
- Prefer `py -3.12 .\run_agent.py` for running the working solution.
- If using `worker/main.py`, keep it compatible with the OpenAI SDK and avoid direct `agents` imports.

---

## 5. Problem: Missing `requirements.txt` in this repo path
- **Issue:** The current workspace root does not contain a `requirements.txt` file visible from the file system scan.
- **Impact:** It is harder to know exact dependencies and package versions.

### Solution
- Use the existing `run_agent.py` working path and install dependencies manually if needed:
  - `openai`
  - `python-dotenv`
  - `requests`
  - `mcp[cli]`
- Ensure the local `.env` file contains `GEMINI_API_KEY` or `OPENAI_API_KEY`.

---

# Video Script

## 1. Intro
"Hello friends, I am [your name]. Today I will show you how I connected the OpenAI Agents SDK with an MCP server and what problems I faced. This project is in the `Agents+MCP` repository."

## 2. Project structure
"The project has two main folders:
- `OpenAI_Agents_SDK_Practice`, where the agent code is located
- `MCP/MCP_Handsoff`, where the MCP server tool definitions are located

And `worker/main.py` was the file that started the agent entrypoint."

## 3. Problem explanation
"When I ran `worker/main.py`, I got this error:
`KeyError: ~TContext`.
This error happened while importing the `agents` library. That means `from agents import Agent, Runner` and `from agents.mcp import MCPServerStdio` failed.

I discovered that this was a Python 3.11 compatibility issue. The repo docs also recommend using Python 3.12 or the direct OpenAI SDK."

## 4. Root cause
"The root cause was:
- the `agents` library failed type hint parsing in Python 3.11
- `worker/main.py` was fully dependent on the `agents` SDK
- if the `agents` import fails, the agent workflow stops immediately"

## 5. Fix strategy
"What I did:
- removed `agents` imports from `worker/main.py`
- switched to direct OpenAI SDK usage (`openai.OpenAI`)
- defined tools using a JSON schema and handled tool calls from the model
- started the MCP server as a subprocess, while agent logic runs with the OpenAI SDK

This avoided the `agents` package crash."

## 6. MCP connection
"The MCP server is still used, but only as a server process:
- `MCP_Handsoff/main.py` runs as a background process
- it contains math and string tool definitions
- if the agent model chooses a tool, we execute that tool in Python

I also added local tool handlers: `add`, `multiply`, `divide`, `reverse_string`, `to_uppercase`, `weather_tool`."

## 7. Problems faced
"Problems I faced:
1. `KeyError: ~TContext` from the `agents` package
2. Python version mismatch (3.11 vs 3.12)
3. old worker implementation broken due to library incompatibility
4. `agents` MCP integration not stable in this repo
5. dependency tracking unclear because `requirements.txt` was missing"

## 8. Result
"Now `worker/main.py` is updated and syntax-error free.
You can use `run_agent.py`, because it is the repo’s working solution.
And if you need to fix Python dependencies, set `GEMINI_API_KEY` or `OPENAI_API_KEY` in `.env`."

## 9. CTA
"If you liked this video, please like, comment, and share it on LinkedIn. I will cover MCP tool extension and agent workflow in more detail in the next video."
