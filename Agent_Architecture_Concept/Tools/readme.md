# Tools in OpenAI Agents SDK

## Overview

Tools allow agents to perform actions beyond generating text, such as:

-   Fetching data
-   Running code
-   Calling external APIs
-   Using computers
-   Executing custom functions

The SDK supports multiple tool categories.

------------------------------------------------------------------------

# Tool Categories

## 1. Hosted OpenAI Tools

These tools run on OpenAI servers alongside the model.

Available tools:

-   **WebSearchTool**: Search the web.
-   **FileSearchTool**: Retrieve information from OpenAI Vector Stores.
-   **CodeInterpreterTool**: Execute code in a sandbox environment.
-   **HostedMCPTool**: Connect remote MCP servers.
-   **ImageGenerationTool**: Generate images from prompts.
-   **ToolSearchTool**: Load deferred tools dynamically.

------------------------------------------------------------------------

## 2. Hosted Tool Search

Tool Search allows models to load only required tools at runtime instead
of exposing every tool initially.

Benefits:

-   Reduces tool schema tokens.
-   Useful when many tools exist.
-   Improves efficiency.

Supported surfaces:

-   Deferred function tools using `defer_loading=True`
-   Tool namespaces
-   Hosted MCP tools

Important:

-   Available only with OpenAI Responses models.
-   Add exactly one `ToolSearchTool()` when using deferred tools.

------------------------------------------------------------------------

# 3. Local Runtime Tools

Local runtime tools execute inside your own environment.

Available tools:

-   `ComputerTool`
-   `ShellTool`
-   `LocalShellTool`
-   `ApplyPatchTool`

The application provides the actual implementation.

Examples:

-   Browser automation
-   Running shell commands
-   Editing files

------------------------------------------------------------------------

# 4. Function Tools

Any Python function can become an agent tool.

The SDK automatically creates:

-   Tool name from function name
-   Description from docstring
-   Input schema from function parameters

Using:

``` python
@function_tool
def my_tool():
    pass
```

The SDK uses:

-   Python inspect module
-   Type annotations
-   Pydantic schemas
-   Docstring parsing

------------------------------------------------------------------------

# Custom FunctionTool

You can manually create a `FunctionTool`.

Required:

-   `name`
-   `description`
-   `params_json_schema`
-   `on_invoke_tool`

This gives full control over tool execution.

------------------------------------------------------------------------

# Tool Output Types

Function tools can return:

-   Text
-   Images
-   Files
-   Structured outputs

Supported types:

-   `ToolOutputText`
-   `ToolOutputImage`
-   `ToolOutputFileContent`

------------------------------------------------------------------------

# Tool Argument Validation

Arguments can be controlled using Pydantic `Field`.

Supported validations:

-   Minimum/maximum values
-   String length
-   Patterns
-   Descriptions

------------------------------------------------------------------------

# Function Tool Timeouts

Async function tools support timeout handling.

Options:

## error_as_result

Returns timeout information to the model.

## raise_exception

Raises `ToolTimeoutError`.

Custom timeout messages can also be provided.

------------------------------------------------------------------------

# Error Handling

Function tools support custom error handling.

`failure_error_function` can:

-   Return friendly error messages
-   Handle tool failures
-   Control how errors are shown to the model

------------------------------------------------------------------------

# Agents as Tools

An agent can be exposed as a tool using:

``` python
agent.as_tool()
```

This allows one agent to call another agent without a handoff.

Useful for:

-   Agent orchestration
-   Specialized tasks
-   Multi-agent workflows

------------------------------------------------------------------------

# Agent Tool Customization

`Agent.as_tool()` supports:

-   max_turns
-   run_config
-   hooks
-   session
-   conversation_id
-   needs_approval
-   structured inputs

------------------------------------------------------------------------

# Structured Input for Agent Tools

By default, `Agent.as_tool()` accepts:

``` json
{
  "input": "text"
}
```

You can provide structured schemas using:

-   Pydantic models
-   Dataclasses

Options:

-   `parameters`
-   `include_input_schema`
-   `input_builder`

------------------------------------------------------------------------

# Approval Gates for Agent Tools

`Agent.as_tool(..., needs_approval=...)`

uses the same approval flow as function tools.

When approval is required:

1.  Run pauses.
2.  Pending approval appears.
3.  State is saved.
4.  Run resumes after approve/reject decision.

------------------------------------------------------------------------

# Custom Output Extraction

You can modify nested agent output before returning it.

Use:

``` python
custom_output_extractor
```

Common uses:

-   Extract JSON
-   Convert formats
-   Validate output
-   Provide fallback values

------------------------------------------------------------------------

# Streaming Nested Agent Runs

`on_stream` allows receiving events from nested agent execution.

Events include:

-   Response events
-   Tool events
-   Agent updates

------------------------------------------------------------------------

# Conditional Tool Enabling

Tools can be dynamically enabled or disabled.

Using:

``` python
is_enabled
```

It supports:

-   Boolean values
-   Sync functions
-   Async functions

Uses:

-   User permissions
-   Feature flags
-   Environment conditions
-   Runtime filtering

Disabled tools are hidden from the model.

------------------------------------------------------------------------

# Experimental: Codex Tool

Codex tool allows agents to run workspace-based tasks.

Capabilities:

-   Shell commands
-   File editing
-   MCP tools

Configuration includes:

-   Workspace directory
-   Sandbox mode
-   Model settings
-   Approval policy
-   Session persistence

------------------------------------------------------------------------

# Summary

    Tools
     |
     |-- Hosted OpenAI Tools
     |-- Tool Search
     |-- Local Runtime Tools
     |-- Function Tools
     |-- Agents as Tools
     |-- Codex Tool

    Function Tools
     |
     |-- Python functions as tools
     |-- Automatic schema creation
     |-- Validation
     |-- Timeout handling
     |-- Error handling

    Agents as Tools
     |
     |-- Agent-to-agent calling
     |-- Structured input
     |-- Approval support
     |-- Streaming support
