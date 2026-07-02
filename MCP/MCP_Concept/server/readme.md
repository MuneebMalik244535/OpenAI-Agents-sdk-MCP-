# 🚀 Understanding MCP Servers

> Beginner-friendly GitHub README with Mermaid diagrams.

## What is an MCP Server?

An **MCP Server** is a program that provides capabilities (tools, resources, and prompts) to AI applications.

```mermaid
flowchart TD
U(User) --> H(Host / ChatGPT)
H --> C(MCP Client)
C --> S(MCP Server)
S --> E(External System)
E --> S
S --> C
C --> H
H --> U
```

## Core Server Features

```mermaid
graph TD
A[MCP Server] --> B[Tools]
A --> C[Resources]
A --> D[Prompts]
```

# 🔨 Tools

**Tools perform actions.**

Examples:
- Search Flights
- Send Email
- Create Calendar Event
- Query Database

**Memory:** Tools = **DO**

```mermaid
flowchart LR
User --> AI
AI --> Tool
Tool --> API
API --> Result
Result --> AI
AI --> User
```

# 📖 Resources

**Resources provide read-only information.**

Examples:
- Files
- PDFs
- Database Records
- Calendar Data

**Memory:** Resources = **READ**

```mermaid
flowchart LR
User --> AI
AI --> Resource
Resource --> Information
Information --> AI
AI --> User
```

Example URI:

```
file:///Documents/resume.pdf
calendar://events/2026
weather://forecast/{city}/{date}
```

# 📝 Prompts

**Prompts are reusable templates started by the user.**

**Memory:** Prompts = **GUIDE**

```mermaid
flowchart LR
User --> Prompt
Prompt --> AI
AI --> Resources
AI --> Tools
Tools --> Result
Result --> User
```

## Feature Comparison

| Feature | Purpose | Controlled By |
|----------|----------|---------------|
| 🔨 Tools | Perform actions | AI Model |
| 📖 Resources | Provide information | Application |
| 📝 Prompts | Reusable workflows | User |

## Complete Workflow

```mermaid
flowchart TD
User --> Prompt
Prompt --> AI
AI --> Resources
Resources --> Context
Context --> AI
AI --> Tools
Tools --> ExternalSystems
ExternalSystems --> Results
Results --> AI
AI --> User
```

## Real-World Example

User: **Plan my vacation to Barcelona**

1. User selects **Plan Vacation** prompt.
2. AI reads resources (calendar, preferences, past trips).
3. AI uses tools (search flights, check weather, book hotel, create calendar event).
4. AI returns the final travel plan.

## Interview Summary

- **Tools = DO**
- **Resources = READ**
- **Prompts = GUIDE**
