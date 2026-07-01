# Guardrails 
### Guardrails are safety rules/checks that control what goes into an AI agent and what comes out of an AI agent.

### Guardrails workflow :
here is the way that explain how guardrails work

User Message
      |
      ↓
Input Guardrail
      |
      ↓
AI Agent
      |
      ↓
Output Guardrail
      |
      ↓
User Response

## Why do we need Guardrails?
Here is a scenario : 

Imagine you built an AI customer support agent.
You are using a powerful AI model like GPT-5.

This model is:
Very smart ✅
Expensive to use 💰
Sometimes slower than smaller models 🐢

Your agent's job is to answer customer support questions, like:
"Where is my order?"
"How can I change my address?"
"I want a refund."

### Without Guardrails

A user sends a wrong request:

"Solve my physics homework step by step."

But your AI agent is not made for homework. It is only for customer support.

Without any protection:

User
  |
  ↓
Expensive AI Model
  |
  ↓
Solves homework

The expensive model spends time and tokens answering something unrelated.

Problems:
You waste money 💰
The AI is used for the wrong purpose
Your system becomes easier to misuse

### With Guardrails

A guardrail works like a security check before the main AI model.

First, the user's message goes to a small and fast AI model.

User
  |
  ↓
Guardrail Model
  |
  ↓
Check the request

The guardrail checks:
"Is this request related to customer support?"

It sees:
"This is a physics homework question."
So it blocks the request.

User
  |
  ↓
Cheap Guardrail Model
  |
  ↓
Detects: Homework request
  |
  ↓
STOP ❌
  |
  ↓
Expensive AI Model never runs

Result:
1. Cost is saved 💰
The expensive model does not run, so you save API costs.

2. Security improves 🔒
Users cannot easily misuse your AI system.

3. Better control 🎯
Your AI only handles tasks it was designed for.

## There are three types of Guardrails are here : 

### 1. Input Guardrails
It checks user input 

User Input
     |
     ↓
Input Guardrail
     |
     ↓
   Agent

User:
"Give me instructions to hack a server"

Input guardrail:
Detected harmful request

BLOCK ❌

### 2. Output Guardrails
It check Final answer of Agents

Flow:

  User
   |
   ↓
 Agent
   |
   ↓
 AI Response
   |
   ↓
 Output Guardrail
   |
   ↓
  User

Example:
Agent generate answer :
Your password is 12345

Output guardrail:
Sensitive information detected
BLOCK

### 3. Tools Guardrails
It protects the tools

Example:
Agent has a tool:

delete_customer()

Agent call this tool by mistake :

Agent
 |
 ↓
delete_customer()
 |
 ↓
Tool Guardrail
 |
 ↓
Allow / Block

## What is meant by Tripwire ?
It's like an alarm when it become True so agent execution stop 

### Different types of execution mode : 
There are two kinds of way of execution mode 

## 1. Parallel Execution (By Default)
It means Agents and Guardrails both start together

### Advantage 
Fast response

### Problem
later if guardrail say its wrong 
so agent has executed task and tokens has been used and tools can run 

## 2. Blocking Execution 
Guardrail start first then Agent start 

User

 ↓

Guardrail

 ↓

Approved?

 ↓

Agent starts

### Benefits:
Token saving
Tool execution prevent
More secure

## Real world Complete Example of Guardrail Each and every concept
### Customer Support AI

Here is an Architecture

                 User
                   |
                   ↓

          Input Guardrail
                   |
                   ↓

        Customer Support Agent

              /          \

             ↓            ↓

       Refund Tool     Email Tool

             |            |

      Tool Guardrail Tool Guardrail


                   ↓

          Output Guardrail

                   ↓

                User

                