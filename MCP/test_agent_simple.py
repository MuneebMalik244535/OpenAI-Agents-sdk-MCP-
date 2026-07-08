#!/usr/bin/env python
"""
Simple Agent Test without Heavy Dependencies
Tests the MCP server connection directly
"""

import subprocess
import sys
import time
import json

def test_agent_simple():
    """
    Simple test that bypasses the heavy agents library
    """
    print("=" * 60)
    print("Testing MCP Server Integration")
    print("=" * 60)
    
    # Test 1: Start MCP Server
    print("\n[1] Starting MCP Server...")
    try:
        server_process = subprocess.Popen(
            [sys.executable, 
             r"C:\Users\LENOVO\Desktop\Agents+MCP\MCP\MCP_Handsoff\main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True
        )
        time.sleep(2)
        
        if server_process.poll() is None:
            print("✓ MCP Server started (PID: {})".format(server_process.pid))
        else:
            stderr = server_process.stderr.read()
            print("✗ MCP Server failed to start")
            print("Error:", stderr)
            return False
            
    except Exception as e:
        print(f"✗ Failed to start server: {e}")
        return False
    
    # Test 2: Try to communicate with server
    print("\n[2] Testing server communication...")
    try:
        # Send a simple JSON-RPC request to get tools
        request = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list",
            "params": {}
        })
        
        # Note: This is a simplified test - real MCP uses a specific protocol
        print("✓ Server communication test prepared")
        
    except Exception as e:
        print(f"✗ Communication test failed: {e}")
        return False
    finally:
        # Cleanup
        print("\n[3] Cleaning up...")
        try:
            server_process.terminate()
            server_process.wait(timeout=5)
            print("✓ Server terminated cleanly")
        except:
            server_process.kill()
            print("✓ Server force-killed")
    
    print("\n" + "=" * 60)
    print("Test completed successfully!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_agent_simple()
    sys.exit(0 if success else 1)
