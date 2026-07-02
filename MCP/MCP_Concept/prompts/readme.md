# MCP Server Features --- Prompts

> **Draft Specification**

## What are Prompts?

The **Model Context Protocol (MCP)** allows servers to expose **Prompt
Templates** to clients.

A prompt is a **predefined template** that users can select instead of
writing long instructions manually.

### Example

``` text
/code_review
```

Instead of writing:

``` text
Please review my Python code and suggest improvements...
```

The server already contains that template.

------------------------------------------------------------------------

# User Interaction Model

-   Prompts are **user-controlled**.
-   The **server defines** the prompt.
-   The **user decides when to use it**.

``` mermaid
flowchart LR
User --> Client
Client -->|"prompts/get"| MCP_Server
MCP_Server --> Prompt_Template
Prompt_Template --> AI_Model
AI_Model --> Response
```

------------------------------------------------------------------------

# Capabilities

Servers declare prompt support.

``` json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` means the server can notify clients whenever the prompt
list changes.

------------------------------------------------------------------------

# Listing Prompts (`prompts/list`)

The client requests available prompts.

``` json
{
  "method":"prompts/list"
}
```

Response contains:

-   name
-   title
-   description
-   arguments
-   icons

Supports:

-   Pagination
-   Caching

------------------------------------------------------------------------

# Getting a Prompt (`prompts/get`)

The client requests a specific prompt.

``` json
{
  "method":"prompts/get",
  "params":{
    "name":"code_review",
    "arguments":{
      "code":"print('Hello')"
    }
  }
}
```

Server returns the final prompt messages.

``` mermaid
sequenceDiagram
participant User
participant Client
participant Server
User->>Client: Select code_review
Client->>Server: prompts/get
Server-->>Client: Prompt Messages
Client-->>User: Execute with AI
```

------------------------------------------------------------------------

# InputRequiredResult

If required information is missing, the server asks for more input
before generating the prompt.

Example:

-   Resume Generator
-   Missing Name
-   Missing Skills

Client collects the missing information and retries.

------------------------------------------------------------------------

# Prompt Data Structure

  Field         Description
  ------------- ----------------------
  name          Unique ID
  title         Human readable title
  description   Prompt description
  arguments     Input parameters
  icons         UI icons

------------------------------------------------------------------------

# Prompt Message Content Types

## Text

``` json
{"type":"text","text":"Explain this code"}
```

## Image

``` json
{"type":"image","mimeType":"image/png"}
```

## Audio

``` json
{"type":"audio","mimeType":"audio/wav"}
```

## Resource Link

Returns only a URI.

``` json
{
"type":"resource_link",
"uri":"file:///project/main.py"
}
```

## Embedded Resource

Resource content is returned directly.

``` json
{
"type":"resource",
"resource":{
"uri":"resource://example",
"text":"Resource content"
}
}
```

------------------------------------------------------------------------

# List Changed Notification

When prompts change:

``` text
notifications/prompts/list_changed
```

Client refreshes the prompt list.

``` mermaid
flowchart TD
Developer --> AddPrompt
AddPrompt --> Server
Server --> Notification
Notification --> Client
Client --> Refresh["prompts/list"]
```

------------------------------------------------------------------------

# Error Handling

  Error                   Code
  ----------------------- --------
  Invalid prompt          -32602
  Missing arguments       -32602
  Internal server error   -32603

------------------------------------------------------------------------

# Implementation Considerations

-   Validate arguments.
-   Handle pagination.
-   Respect capability negotiation.
-   Use cache when possible.

------------------------------------------------------------------------

# Security

Always validate:

-   User input
-   Prompt output
-   Resource access

This prevents:

-   Prompt Injection
-   Unauthorized Access

------------------------------------------------------------------------

# Complete Flow

``` mermaid
flowchart TD
A[User] --> B[Choose Prompt]
B --> C[Client]
C --> D[prompts/list]
D --> E[MCP Server]
E --> F[Prompt List]
F --> C
C --> G[prompts/get]
G --> E
E --> H[Prompt Messages]
H --> I[AI Model]
I --> J[Final Response]
```

------------------------------------------------------------------------

# Summary

-   **Prompts** = Ready-made prompt templates.
-   **Users** choose prompts.
-   **Clients** discover and fetch prompts.
-   **Servers** define and manage prompts.
-   Supports pagination, caching, notifications, and secure validation.
