#!/usr/bin/env python
"""Simple test to verify MCP server is working"""

import subprocess
import time
import json
import sys

def test_mcp_server():
    """Test if MCP server can be started and responds"""
    print("Starting MCP Server...")
    
    # Start the MCP server
    try:
        process = subprocess.Popen(
            [sys.executable, 
             r"C:\Users\LENOVO\Desktop\Agents+MCP\MCP\MCP_Handsoff\main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        time.sleep(2)  # Give server time to start
        
        # Check if process is still running
        if process.poll() is None:
            print("✓ MCP Server started successfully")
            print("✓ Server is running (PID: {})".format(process.pid))
            
            # Try to terminate gracefully
            process.terminate()
            process.wait(timeout=5)
            print("✓ Server terminated cleanly")
            return True
        else:
            stdout, stderr = process.communicate()
            print("✗ MCP Server failed to start")
            print("STDOUT:", stdout)
            print("STDERR:", stderr)
            return False
            
    except Exception as e:
        print(f"✗ Error testing MCP server: {e}")
        return False

if __name__ == "__main__":
    success = test_mcp_server()
    sys.exit(0 if success else 1)
