#!/usr/bin/env python
"""
Practical Agent with MCP Integration
Uses OpenAI SDK directly without the problematic agents library
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

# Get API key
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: No API key found. Set GEMINI_API_KEY or OPENAI_API_KEY in .env")
    sys.exit(1)

# Initialize OpenAI client (for Gemini)
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# MCP Server process
mcp_process = None

def start_mcp_server():
    """Start the MCP server in background"""
    global mcp_process
    
    print("[STARTUP] Starting MCP Server...")
    mcp_path = r"C:\Users\LENOVO\Desktop\Agents+MCP\MCP\MCP_Handsoff\main.py"
    
    if not Path(mcp_path).exists():
        print(f"ERROR: MCP server not found at {mcp_path}")
        return False
    
    try:
        mcp_process = subprocess.Popen(
            [sys.executable, mcp_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        )
        time.sleep(1)  # Give server time to start
        
        if mcp_process.poll() is None:
            print(f"[STARTUP] ✓ MCP Server started (PID: {mcp_process.pid})")
            return True
        else:
            print("[STARTUP] ✗ MCP Server failed to start")
            return False
    except Exception as e:
        print(f"[STARTUP] ✗ Error starting MCP server: {e}")
        return False

def stop_mcp_server():
    """Stop the MCP server"""
    global mcp_process
    
    if mcp_process:
        try:
            mcp_process.terminate()
            mcp_process.wait(timeout=3)
        except:
            try:
                mcp_process.kill()
            except:
                pass
        print("[SHUTDOWN] ✓ MCP Server stopped")

def call_agent(user_message: str) -> str:
    """Call the agent with user message"""
    
    # Define available MCP tools
    tools = [
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
        }
    ]
    
    messages = [
        {
            "role": "user",
            "content": user_message
        }
    ]
    
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=1024
        )
        
        # Get the response
        message = response.choices[0].message
        
        # If there's text content, return it
        if message.content:
            return message.content
        
        # If there are tool calls, handle them
        if hasattr(message, 'tool_calls') and message.tool_calls:
            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            
            # Simulate tool execution
            result = f"[Tool: {tool_name}] Called with {tool_args}"
            return result
        
        return "No response generated"
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main agent loop"""
    
    print("=" * 70)
    print("AI Agent with MCP Tools Integration")
    print("=" * 70)
    print()
    
    # Start MCP server
    if not start_mcp_server():
        print("[ERROR] Could not start MCP server")
        return
    
    print("\n[INFO] Available tools:")
    print("  • Math: add, multiply, divide")
    print("  • String: reverse_string, to_uppercase")
    print("\n[INFO] Type 'quit' or 'exit' to stop\n")
    
    try:
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                
                print("[Agent] Processing...")
                response = call_agent(user_input)
                print(f"[Agent] {response}\n")
                
            except KeyboardInterrupt:
                print("\n[Interrupted]")
                break
                
    finally:
        stop_mcp_server()
        print("\n[SHUTDOWN] Agent stopped.")

if __name__ == "__main__":
    main()
