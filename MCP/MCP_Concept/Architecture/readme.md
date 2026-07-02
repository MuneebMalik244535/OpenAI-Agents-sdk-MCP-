# MCP Architecture Overview

> Beginner-friendly notes for understanding the **Model Context Protocol
> (MCP)** architecture.

------------------------------------------------------------------------

# What is MCP?

**Model Context Protocol (MCP)** is an open standard that allows AI
applications to communicate with external tools, services, databases,
and data sources using one common protocol.

### Simple Definition

> **MCP is like a USB-C port for AI.**

Instead of creating a different connection for every tool, AI
applications use MCP as one standard way to communicate.

------------------------------------------------------------------------

# Why Does MCP Matter?

Without MCP:

-   Every AI application needs separate integrations.
-   More code.
-   More maintenance.
-   Hard to scale.

With MCP:

-   One protocol.
-   Many tools.
-   Easy integration.
-   Better developer experience.

------------------------------------------------------------------------

# MCP Scope

MCP is made up of four major parts.

## 1. MCP Specification

The official rulebook.

It defines:

-   How Clients work
-   How Servers work
-   How communication happens

------------------------------------------------------------------------

## 2. MCP SDKs

SDK = Software Development Kit.

SDKs provide ready-made code so developers don't need to build
everything from scratch.

Example:

``` python
await session.call_tool(...)
```

------------------------------------------------------------------------

## 3. MCP Development Tools

Tools that help developers build and debug MCP applications.

Example:

-   MCP Inspector

------------------------------------------------------------------------

## 4. Reference Servers

Ready-made example MCP servers that developers can study or extend.

------------------------------------------------------------------------

# MCP Participants

Every MCP application contains three main participants.

    Host
     │
    Client
     │
    Server

------------------------------------------------------------------------

## MCP Host

The Host is the AI application.

Examples

-   ChatGPT
-   Claude Desktop
-   Claude Code
-   Cursor
-   VS Code

The Host manages one or more MCP Clients.

------------------------------------------------------------------------

## MCP Client

The Client is responsible for:

-   Connecting to an MCP Server
-   Sending requests
-   Receiving responses

Every server has its own dedicated client.

------------------------------------------------------------------------

## MCP Server

The Server provides:

-   Tools
-   Resources
-   Prompts
-   Context

Examples

-   Filesystem Server
-   Database Server
-   GitHub Server
-   Weather Server

------------------------------------------------------------------------

# Overall Flow

    You
     │
     ▼
    Host
     │
     ▼
    MCP Client
     │
     ▼
    MCP Server
     │
     ▼
    External Tool
     │
     ▼
    Response
     │
     ▼
    Host
     │
     ▼
    You

------------------------------------------------------------------------

# One Host → Multiple Clients

A Host can connect to many MCP Servers.

                  Host
                    │
          ┌─────────┼─────────┐
          │         │         │
       Client1   Client2   Client3
          │         │         │
     Filesystem Database GitHub
       Server     Server   Server

Each Client manages exactly one Server connection.

------------------------------------------------------------------------

# Local vs Remote MCP Servers

## Local Server

Runs on your own computer.

Example

    Host
     │
    Client
     │
    Filesystem Server

Uses **STDIO Transport**.

------------------------------------------------------------------------

## Remote Server

Runs on another computer or cloud service.

Example

    Host
     │
    Internet
     │
    GitHub MCP Server

Uses **HTTP Transport**.

------------------------------------------------------------------------

# MCP Layers

MCP has two layers.

    Transport Layer
           │
    Data Layer

------------------------------------------------------------------------

# Data Layer

The Data Layer defines **what information is exchanged**.

It includes:

-   JSON-RPC messages
-   Tools
-   Resources
-   Prompts
-   Notifications
-   Lifecycle

Example

User asks:

> What's the weather?

Client sends a JSON request.

Server returns weather data.

------------------------------------------------------------------------

# Transport Layer

The Transport Layer defines **how information travels**.

Supported transports:

## STDIO

-   Local communication
-   Same machine
-   Fast
-   No internet

## Streamable HTTP

-   Remote communication
-   Internet
-   Supports authentication
-   API Keys
-   OAuth
-   Bearer Tokens

------------------------------------------------------------------------

# Lifecycle Management

Lifecycle controls everything from starting a connection until closing
it.

Steps:

1.  Initialize Connection
2.  Version Negotiation
3.  Capability Negotiation
4.  Ready State
5.  Communication
6.  Connection Close

Flow

    Client
     │
    Initialize
     │
    Server
     │
    Check Version
     │
    Check Capabilities
     │
    Ready
     │
    Tool Calls

------------------------------------------------------------------------

# MCP Primitives

Primitives are the core building blocks of MCP.

------------------------------------------------------------------------

## Tools

Tools perform actions.

Examples

-   Search
-   Database Query
-   File Operations
-   API Calls

Think:

> **AI can DO something.**

------------------------------------------------------------------------

## Resources

Resources provide information.

Examples

-   Files
-   Database Records
-   API Responses
-   Documentation

Think:

> **AI can READ something.**

------------------------------------------------------------------------

## Prompts

Reusable prompt templates.

Example

    Summarize professionally.

Think:

> **Reusable instructions.**

------------------------------------------------------------------------

# Client Primitives

Servers can also request help from the Client.

------------------------------------------------------------------------

## Sampling

Server requests the Host's AI model to generate text.

    Server
     │
    Client
     │
    LLM
     │
    Generated Response

------------------------------------------------------------------------

## Elicitation

Server asks the user for more information.

Example

> Which city?

User replies.

Server continues.

------------------------------------------------------------------------

## Logging

Server sends logs for debugging.

Example

    Connecting...
    Loading...
    Done.

------------------------------------------------------------------------

# Notifications

Notifications inform the Client about changes.

No response is expected.

Example

    Server

    ↓

    Tool List Changed

    ↓

    Client

    ↓

    Refresh Tools

------------------------------------------------------------------------

# Tool Discovery

Before calling a Tool, the Client first asks:

> What tools do you have?

Server replies with available tools.

Example

-   Weather
-   Calculator
-   Search
-   GitHub

------------------------------------------------------------------------

# Tool Execution

After discovering a Tool, the Client executes it.

    User

    ↓

    Host

    ↓

    Weather Tool

    ↓

    Weather Server

    ↓

    Weather Result

    ↓

    Host

    ↓

    User

------------------------------------------------------------------------

# Real-Time Updates

If new tools become available,

The Server sends a Notification.

The Client updates its Tool List automatically.

------------------------------------------------------------------------

# Complete MCP Workflow

    User
     │
     ▼
    Host (AI Application)
     │
     ▼
    MCP Client
     │
     ▼
    Initialize
     │
     ▼
    Capability Negotiation
     │
     ▼
    List Tools
     │
     ▼
    Tool Call
     │
     ▼
    MCP Server
     │
     ▼
    External System
    (API / Database / Files)
     │
     ▼
    Result
     │
     ▼
    Host
     │
     ▼
    User

------------------------------------------------------------------------

# USB-C Analogy

  USB-C        MCP
  ------------ ------------------
  Laptop       AI Application
  USB-C Port   MCP
  Keyboard     Tool
  Mouse        Tool
  SSD          Database
  Monitor      External Service

------------------------------------------------------------------------

# Key Takeaways

-   MCP is an open standard for AI communication.
-   Host manages Clients.
-   Client communicates with one Server.
-   Server provides Tools, Resources, and Prompts.
-   One Host can connect to multiple Servers.
-   Data Layer defines **what** is exchanged.
-   Transport Layer defines **how** data travels.
-   Lifecycle initializes and manages connections.
-   Tools perform actions.
-   Resources provide context.
-   Prompts provide reusable instructions.
-   Sampling uses the Host's AI model.
-   Elicitation asks users for additional input.
-   Logging helps debugging.
-   Notifications provide real-time updates.
-   Tool Discovery lists available tools.
-   Tool Execution performs actions.
