## Human In the Loop (HITL)
when an AI agent take important decision or does important action so it stops and take approval or permission from human
### In simple words 
AI agents can take action by itself but sometime it need to take permission or approval from the humans
### points
Instead of giving fully control to AI Agents we just make safety check points 

### Examples 
1. we know very well about firewall on server , when any post is being uploaded or published on the internet server so firewall check all the post if it against of this country or harmfull content for the public it just stop the post 
2. People can visit thier country places without getting permission so the government just make checkpoint for public safety its similar like human in the loop 

### scenarios 
User tell agents to transfer 5000$ to my client and just imagine if the agent transfer wrongly or there will be some hacking issues happened so user will lost his amount 
so we just make human in the loop

### Here is the workflow

User request
      |
      ↓
AI Agent
      |
      ↓
transfer_money()
      |
      ↓
Money sent

### How human in the loop will protect from lost ?
when user tell to agents transfer amount so the agents take decision and before transferring agent ask to user for giving permission or approval to transfer that means it will be double check so in this case we can protect most of 95% amount in the real world 

# Here is the workflow how can we prevent from lossess 

User request
      |
      ↓
AI Agent
      |
      ↓
transfer_money()
      |
      ↓
⛔ Approval Required
      |
      ↓
Human checks
      |
      ↓
Approve / Reject
      |
      ↓
Money transfer

## Lete see how the workflow look like 

Agent starts running

        |
        |
        ↓

Agent decides:
"I need to call this tool"

        |
        |
        ↓

Tool says:
"I need human approval"

        |
        |
        ↓

Run pauses

        |
        |
        ↓

Human reviews request

        |
        |
        ↓

Approve OR Reject

        |
        |
        ↓

Run resumes

### How do you make any tools approval required ? 
"""
from agents import Agent , Runner , function_tool
@function_tool(needs_approval=True)
async def cancel_order(order_id: int) -> str:
    return f"Cancelled order {order_id}"
"""
### Code Login Explain
Here is the word "needs_approval" inside the @function_tool so it make tool approval required or not but just adding login of
True and False
In my Case of code : I just make it "True" because i need to make my tool become approval required in other case if i dont want to make it approval required i just make this login "False"

# Dynamic Approval 
### It just based on Conditions 
If i have refund problem while i will implement some condition on the basis of refund amount
if the refund amount small ----- agent will take decision and let it be given
but in othercase if the refund amount will be large so ---- agent will take approval from human 

"""
async def requires_review(_ctx, params, _call_id):
    return "refund" in params.get("subject", "").lower()
"""
### How this code will work 
If there is a word of "refund" so it required human approval otherwise direct send 
Lets integrate this function logic with Email function_tool

"""
@function_tool(needs_approval=required_review)
async def send_email(subject:str, body:str):
    return f"Sent {subject}"
"""

### Case 1:

Subject:
"Meeting reminder"
AI sends email directly

### Case 2:

Subject:
"Refund request"
AI pauses
Human approval required

## What is RunState ? 
When approval is required for processing further task or action so agent run pause and RunState save agent pause state 
In easy words : RunState == Agent ka current status

Imagine:

Agent:

Step 1:
Understand user

Step 2:
Call refund tool

Step 3:
WAITING FOR APPROVAL

Now you save RunState :

RunState:
{
 current_step:"refund approval",
 pending_tool:"refund_customer",
 status:"waiting"
}

After human decision:

Resume RunState
Agent continue from it

## What is Run-wide approval ? 
If any agent need human approval so the whole agent execution stop until get human approval.

### Simple Analogy...
Imagine a company has an AI customer support system.
This system has different agents:

Customer Support Agent
          |
          ↓
     Billing Agent
          |
          ↓
     Refund Tool

A customer sends a message:
"I want to cancel my order and get my money back."

Step 1: Customer Support Agent

The first agent receives the customer's message.

It thinks:
"This is a refund request. I should send this to the Billing Agent."
So it transfers the task to the Billing Agent.

Customer Support Agent

          ↓

Billing Agent
Step 2: Billing Agent

The Billing Agent checks the information:

Is the order real?
Is this customer the correct owner?
How much money should be refunded?

After checking everything, it decides:
"I need to use the Refund Tool to send the money back."

Billing Agent

          ↓

Refund Tool
Step 3: Refund Tool Needs Human Approval
Now the Refund Tool wants to process the refund.
But refunds are sensitive actions because:

The AI might make a mistake.
It might refund the wrong customer.
It might refund a large amount of money.

So the Refund Tool says:
"Stop. I need human approval before doing this action."

Now Human-in-the-loop (HITL) starts.
What does Run-wide Approval mean?
Imagine approval only worked inside the Billing Agent:

Billing Agent
      |
      ↓
Refund Tool

WAITING FOR APPROVAL
Only the Billing Agent would stop.
But in OpenAI Agents SDK, approval works at the whole run level.

That means the complete workflow stops:

Customer Support Agent
          |
          ↓
    Billing Agent
          |
          ↓
     Refund Tool
          |
          ↓
WAITING FOR HUMAN APPROVAL

The whole process is paused.
What does the Human do?

A human employee opens the approval screen:

Pending Approval:
Customer: Ahmed
Action: Refund $500
Tool: Refund Tool

[Approve]   [Reject]
If Human Approves:

The workflow continues:

Human Approves

        ↓

RunState continues

        ↓

Refund Tool runs

        ↓

Customer receives refund
If Human Rejects:
The refund does not happen.
The system sends a message:
"Your refund request needs manual review."

## What is meant by Agent.as_tool() ?
Normally we create agents and for agents we create tool so that agent will execute task easily with the help of tools 
### How can agent become a tool for another agent ?
For example I have two types of agents 
1. Researcher agent 
2. Writer agent 
I want my Writer agent to write anything by doing research and getting information from other sites 
Infact write agent has no access for doing this so what will be the next way to do this ?
We have researcher agent also who can research and get information from other sites
so we just give researcher agent as a tool to writer agent 
writer agent will use researcher agent as a tool if writer agent will need research or anyother information 

