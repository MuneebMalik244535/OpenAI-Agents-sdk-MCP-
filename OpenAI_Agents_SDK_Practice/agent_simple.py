#!/usr/bin/env python
"""
Direct Agent Implementation using OpenAI SDK
Bypasses the problematic agents library
Connects to MCP server for tools
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

# Load environment
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Initialize OpenAI client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# MCP Server process reference
mcp_process = None

def start_mcp_server():
    """Start the MCP server"""
    global mcp_process
    
    print("Starting MCP Server...")
    mcp_path = r"C:\Users\LENOVO\Desktop\Agents+MCP\MCP\MCP_Handsoff\main.py"
    
    try:
        mcp_process = subprocess.Popen(
            [sys.executable, mcp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True
        )
        time.sleep(2)  # Give server time to start
        
        if mcp_process.poll() is None:
            print("✓ MCP Server started (PID: {})".format(mcp_process.pid))
            return True
        else:
            print("✗ MCP Server failed to start")
            return False
    except Exception as e:
        print(f"✗ Error starting MCP server: {e}")
        return False

def stop_mcp_server():
    """Stop the MCP server"""
    global mcp_process
    
    if mcp_process:
        try:
            mcp_process.terminate()
            mcp_process.wait(timeout=5)
            print("✓ MCP Server stopped")
        except:
            mcp_process.kill()
            print("✓ MCP Server force-killed")

async def call_llm(user_message: str, tools_list: list):
    """Call the LLM with available tools"""
    
    print(f"\n[Agent] User: {user_message}")
    
    system_prompt = """You are a helpful AI Assistant with access to various tools.
Available tools allow you to:
- Perform mathematical operations (add, sub, multiply, divide)
- Manipulate strings (reverse, uppercase, lowercase, length, split, combine)
- Process lists (sum, average, max, min)

Use the tools to help answer user questions. Always explain what you're doing."""
    
    messages = [
        {"role": "user", "content": user_message}
    ]
    
    try:
        # Call LLM
        response = await client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools_list,
            tool_choice="auto",
            max_tokens=1024
        )
        
        # Process response
        assistant_message = response.choices[0].message
        
        if assistant_message.content:
            print(f"[Agent] Assistant: {assistant_message.content}")
        
        return {
            "content": assistant_message.content,
            "tool_calls": getattr(assistant_message, "tool_calls", None)
        }
        
    except Exception as e:
        print(f"[Agent] Error calling LLM: {e}")
        return {"content": "Error calling LLM", "tool_calls": None}

async def main():
    """Main agent loop"""
    
    print("=" * 70)
    print("AI Assistant with MCP Integration")
    print("=" * 70)
    
    # Start MCP server
    if not start_mcp_server():
        print("Failed to start MCP server. Exiting.")
        return
    
    # Define tools (example - would normally come from MCP)
    tools = [
        {
            "type": "function",
            "function": {
                "name": "add",
                "description": "Add two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
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
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            }
        }
    ]
    
    print("\nTools available: add, multiply")
    print("Type 'quit' to exit\n")
    
    try:
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                break
            
            if not user_input:
                continue
            
            response = await call_llm(user_input, tools)
            print()
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    
    finally:
        stop_mcp_server()
        print("\nAgent stopped.")

if __name__ == "__main__":
    asyncio.run(main())
