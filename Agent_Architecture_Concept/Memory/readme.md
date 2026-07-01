# Memory and Session in OpenAI Agents SDK

## Session

**Bases: Protocol**

`Session` is a protocol for session implementations.

A session stores conversation history for a specific session, allowing
agents to maintain context without requiring explicit manual memory
management.

Source: `src/agents/memory/session.py`

------------------------------------------------------------------------

# Session Methods

## get_items()

Retrieves the conversation history for this session.

``` python
get_items(
    limit: int | None = None,
) -> list[TResponseInputItem]
```

### Parameters

  -----------------------------------------------------------------------
  Name              Type              Description       Default
  ----------------- ----------------- ----------------- -----------------
  limit             int \| None       Maximum number of None
                                      items to          
                                      retrieve. If      
                                      None, retrieves   
                                      all items. When   
                                      specified,        
                                      returns latest N  
                                      items in          
                                      chronological     
                                      order.            

  -----------------------------------------------------------------------

### Returns

`list[TResponseInputItem]`

List of input items representing conversation history.

------------------------------------------------------------------------

## add_items()

Adds new items to conversation history.

``` python
add_items(items: list[TResponseInputItem]) -> None
```

### Parameter

  ----------------------------------------------------------------------------
  Name                    Type                         Description
  ----------------------- ---------------------------- -----------------------
  items                   list\[TResponseInputItem\]   List of input items to
                                                       add to history

  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## pop_item()

Removes and returns the most recent item from the session.

``` python
pop_item() -> TResponseInputItem | None
```

Returns the latest item if it exists, otherwise `None`.

------------------------------------------------------------------------

## clear_session()

Clears all items from the session.

``` python
clear_session() -> None
```

------------------------------------------------------------------------

# SQLiteSession

**Bases: SessionABC**

SQLiteSession is a SQLite-based implementation of session storage.

It stores conversation history in a SQLite database.

By default it uses an in-memory database (`:memory:`), which is deleted
when the process ends. For persistent storage, provide a database file
path.

Source: `src/agents/memory/sqlite_session.py`

------------------------------------------------------------------------

# Initialization

``` python
__init__(
    session_id: str,
    db_path: str | Path = ":memory:",
    sessions_table: str = "agent_sessions",
    messages_table: str = "agent_messages",
    session_settings: SessionSettings | None = None,
)
```

## Parameters

  ------------------------------------------------------------------------
  Name               Type              Description       Default
  ------------------ ----------------- ----------------- -----------------
  session_id         str               Unique identifier Required
                                       for conversation  
                                       session           

  db_path            str \| Path       SQLite database   :memory:
                                       file path         

  sessions_table     str               Table storing     agent_sessions
                                       session metadata  

  messages_table     str               Table storing     agent_messages
                                       message data      

  session_settings   SessionSettings   Session           None
                     \| None           configuration     
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# SQLiteSession Methods

SQLiteSession provides:

-   `get_items()`
-   `add_items()`
-   `pop_item()`
-   `clear_session()`

It also provides:

## close()

Closes the database connection.

``` python
close() -> None
```

------------------------------------------------------------------------

# OpenAIConversationsSession

**Bases: SessionABC**

OpenAIConversationsSession manages conversations using OpenAI
conversation storage.

Source: `src/agents/memory/openai_conversations_session.py`

------------------------------------------------------------------------

# session_id Property

Gets the session ID (conversation ID).

``` python
session.session_id
```

Returns:

`str`

The conversation ID for this session.

### ValueError

If the session has not been initialized yet, accessing `session_id`
raises `ValueError`.

Initialize it by calling:

``` python
await session.get_items()
```

or:

``` python
await session.add_items(...)
```

------------------------------------------------------------------------

# Memory vs Session

## Memory

Memory is a general concept where an AI remembers information.

Examples:

-   User name
-   User preferences
-   Previous facts

## Session

Session is the storage of a specific conversation.

Examples:

-   User messages
-   Assistant responses
-   Conversation history

------------------------------------------------------------------------

# Real World Example

## Customer Support Agent

Without Session:

User: "My order number is 1234."

Later:

User: "Where is my order?"

Agent: "Please provide your order number."

The agent forgot previous context.

------------------------------------------------------------------------

With Session:

User: "My order number is 1234."

Session stores this information.

Later:

User: "Where is my order?"

Agent: "Checking order number 1234."

------------------------------------------------------------------------

# Complete Flow

    User
     |
     ↓
    Session
     |
     ↓
    Agent
     |
     ↓
    Response

Session keeps conversation history for future interactions.

------------------------------------------------------------------------

# When to Use SQLiteSession?

Use SQLiteSession when:

-   Building production applications
-   You need persistent memory
-   Multiple users have separate sessions
-   Data should survive application restart

Examples:

-   Customer support chatbot
-   AI tutor
-   Personal assistant
-   Sales assistant

------------------------------------------------------------------------

# When to Use In-Memory Session?

Use:

``` python
db_path=":memory:"
```

For:

-   Testing
-   Development
-   Temporary conversations

------------------------------------------------------------------------

# Interview Answer

Session in OpenAI Agents SDK is a mechanism that stores conversation
history for an agent, allowing it to maintain context across multiple
interactions. It provides methods like `get_items`, `add_items`,
`pop_item`, and `clear_session`. SQLiteSession provides persistent
storage using SQLite, while OpenAIConversationsSession manages
conversations using OpenAI conversation storage.

------------------------------------------------------------------------

# Summary

    Session
     |
     |-- Stores conversation history
     |-- Maintains context
     |-- Provides memory management

    get_items()
     |
     ↓
    Retrieve history

    add_items()
     |
     ↓
    Save messages

    pop_item()
     |
     ↓
    Remove latest message

    clear_session()
     |
     ↓
    Delete session data

    SQLiteSession
     |
     ↓
    SQLite based persistent memory

    OpenAIConversationsSession
     |
     ↓
    OpenAI conversation storage
