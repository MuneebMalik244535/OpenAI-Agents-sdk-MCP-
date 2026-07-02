# Understanding MCP Clients

> Beginner-friendly notes for **MCP Clients** with simple explanations
> and diagrams.

------------------------------------------------------------------------

# What is an MCP Client?

An **MCP Client** is created by the **Host** (ChatGPT, Claude, VS Code,
Cursor, etc.) to communicate with **one MCP Server**.

    User
      │
      ▼
    Host (ChatGPT / Claude)
      │
      ▼
    MCP Client
      │
      ▼
    MCP Server

**Important:** One MCP Client connects to **only one** MCP Server.

------------------------------------------------------------------------

# Core Client Features

An MCP Client provides three important features to servers:

  Feature       Purpose
  ------------- ----------------------------------------
  Elicitation   Ask the user for missing information
  Roots         Tell the server which folders to use
  Sampling      Let the server use the Host's AI model

------------------------------------------------------------------------

# 1. Elicitation

## Definition

**Elicitation** allows a server to ask the user for missing information
through the client.

    Server
      │
      ▼
    Client
      │
      ▼
    Ask User
      │
      ▼
    User Response
      │
      ▼
    Server Continues

## Real-World Example

User:

> Book a flight to Dubai.

The server needs more information:

-   Window or aisle seat?
-   Hotel required?
-   Travel insurance?

The client asks the user these questions, sends the answers back to the
server, and the booking continues.

### Key Point

> Elicitation = **Ask the user for missing information.**

------------------------------------------------------------------------

# 2. Roots

## Definition

**Roots** tell the server which folders or directories it should work
with.

    Computer
    ├── Projects
    ├── Downloads
    ├── Photos
    └── Documents

    Root Selected
          │
          ▼
    Projects

The server should focus only on the selected root.

## Real-World Example

VS Code opens:

    Travel-App/

The client tells the server:

    Root
     │
     ▼
    Travel-App/

Now the server mainly works inside **Travel-App**.

> **Note:** Roots help define the working area, but they are **not** a
> security system. File permissions are still controlled by the
> operating system.

### Key Point

> Roots = **Tell the server where to work.**

------------------------------------------------------------------------

# 3. Sampling

## Definition

**Sampling** allows the server to use the Host's AI model through the
client.

    Server
      │
      ▼
    Client
      │
      ▼
    LLM (GPT / Claude)
      │
      ▼
    Generated Answer
      │
      ▼
    Server

## Real-World Example

A travel server finds **47 flights**.

Instead of choosing the best flight itself, it asks the client's AI
model to analyze them.

The AI recommends the best option and sends the result back to the
server.

### Human Approval

    Server
       │
    Sampling Request
       │
    Client
       │
    Approve?
       │
    User

The user can approve or reject the request.

### Key Point

> Sampling = **The server uses the Host's AI model through the client.**

------------------------------------------------------------------------

# Feature Comparison

  Feature       Easy Meaning
  ------------- --------------------------------------------
  Elicitation   Ask the user for missing information
  Roots         Tell the server which folders to use
  Sampling      Use the Host's AI model through the client

------------------------------------------------------------------------

# Complete Workflow

    User
     │
     ▼
    Host
     │
     ▼
    MCP Client
     ├───────────────┐
     │               │
     ▼               ▼
    Elicitation   Roots
     │               │
     ▼               ▼
    Ask User     Select Folder
     │
     ▼
    Sampling
     │
     ▼
    LLM
     │
     ▼
    MCP Server
     │
     ▼
    Final Result

------------------------------------------------------------------------

# Interview Summary

-   **Elicitation:** The server asks the user for additional information
    through the client.
-   **Roots:** The client tells the server which directories it should
    focus on.
-   **Sampling:** The server requests the client to use the Host's AI
    model for AI-generated output while keeping user control and
    security.
