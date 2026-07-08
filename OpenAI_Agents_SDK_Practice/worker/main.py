#!/usr/bin/env python
"""
Worker agent entrypoint updated to use the OpenAI SDK directly.
This avoids the broken `agents` library import on Python 3.11.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import requests

# Load environment variables from the project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

# Initialize OpenAI client
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: No API key found. Set GEMINI_API_KEY or OPENAI_API_KEY in .env")
    sys.exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

mcp_process = None

MCP_SERVER_PATH = Path(r"C:\Users\LENOVO\Desktop\Agents+MCP\MCP\MCP_Handsoff\main.py")

LOCAL_TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "divide",
            "description": "Divide two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "Numerator"},
                    "b": {"type": "number", "description": "Denominator"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "reverse_string",
            "description": "Reverse a string",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to reverse"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "to_uppercase",
            "description": "Convert text to uppercase",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to convert"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "weather_tool",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"]
            }
        }
    }
]


def start_mcp_server() -> bool:
    global mcp_process

    if not MCP_SERVER_PATH.exists():
        print(f"ERROR: MCP server not found at {MCP_SERVER_PATH}")
        return False

    try:
        mcp_process = subprocess.Popen(
            [sys.executable, str(MCP_SERVER_PATH)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
        time.sleep(1)
        if mcp_process.poll() is None:
            print(f"[STARTUP] MCP Server started (PID: {mcp_process.pid})")
            return True

        print("[STARTUP] MCP Server failed to start")
        return False
    except Exception as exc:
        print(f"[STARTUP] Error starting MCP server: {exc}")
        return False


def stop_mcp_server() -> None:
    global mcp_process
    if mcp_process:
        try:
            mcp_process.terminate()
            mcp_process.wait(timeout=3)
        except Exception:
            try:
                mcp_process.kill()
            except Exception:
                pass
        print("[SHUTDOWN] MCP Server stopped")


def execute_tool(tool_name: str, arguments: dict) -> str:
    if tool_name == "add":
        return str(arguments["a"] + arguments["b"])
    if tool_name == "multiply":
        return str(arguments["a"] * arguments["b"])
    if tool_name == "divide":
        try:
            return str(arguments["a"] / arguments["b"])
        except ZeroDivisionError:
            return "Error: division by zero"
    if tool_name == "reverse_string":
        return arguments["text"][::-1]
    if tool_name == "to_uppercase":
        return arguments["text"].upper()
    if tool_name == "weather_tool":
        city = arguments.get("city", "")
        if not city:
            return "Error: city name is required"
        response = requests.get(f"https://wttr.in/{city}?format=3")
        return response.text.strip()
    return f"Error: unknown tool {tool_name}"


def call_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=LOCAL_TOOL_DEFINITIONS,
            tool_choice="auto",
            max_tokens=1024,
        )

        message = response.choices[0].message

        if getattr(message, "content", None):
            return message.content

        tool_calls = getattr(message, "tool_calls", None)
        if tool_calls:
            tool_call = tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            tool_result = execute_tool(tool_name, tool_args)
            return f"[Tool: {tool_name}] {tool_result}"

        return "No response generated"
    except Exception as exc:
        return f"Error: {exc}"


def main() -> None:
    print("=" * 60)
    print("AI Assistant with MCP Tools Integration")
    print("=" * 60)
    print("\nAvailable tools:")
    print("- add, multiply, divide, reverse_string, to_uppercase, weather_tool")
    print("\nType 'quit' or 'exit' to stop.\n")

    if not start_mcp_server():
        print("[ERROR] Could not start the MCP server")
        return

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"quit", "exit", "q"}:
                break

            print("[Agent] Processing...")
            response = call_agent(user_input)
            print(f"[Agent] {response}\n")
    except KeyboardInterrupt:
        print("\n[Interrupted]")
    finally:
        stop_mcp_server()
        print("[SHUTDOWN] Agent stopped.")


if __name__ == "__main__":
    main()
