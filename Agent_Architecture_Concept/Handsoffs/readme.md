# What is meant by Handsoff ? 
To transfer One agent work to another agent 

### Why do we need Handsoff?

If you teach one agent everything :
Like : 
Customer Support Agent

- Refund
- Billing
- Technical issue
- Order tracking
- Complaint
- Sales

Problem:

Agent prompt will become so long
There will be confusion too much 
Accuracy can be low

Better approach:

Create Specialized agents :

                Customer

                   |
                   ↓

             Triage Agent
              (Router)

        /        |        \

       ↓         ↓         ↓

 Refund     Billing    Technical
 Agent      Agent       Agent

Every agent is expert on his field

### Handsoff work like a tool for agent
Handsoff is a tool for LLM 

if you write:
handoffs=[refund_agent]

SDK create internally:

Tool:

transfer_to_refund_agent

LLM thinks :
"If i have refund work so , i would call this tool"

### Basic Handoff Example with real code

"""
from agents import Agent, handoff


billing_agent = Agent(
    name="Billing agent"
)


refund_agent = Agent(
    name="Refund agent"
)


triage_agent = Agent(
    name="Triage agent",
    handoffs=[
        billing_agent,
        handoff(refund_agent)
    ]
)
"""
Here :
Triage Agent has two options :

1. transfer_to_billing_agent
2. transfer_to_refund_agent

### Important options of Handsoff
1. Agent
which agent do i transfer this 

2. tool_name_override

Default:
transfer_to_refund_agent

If you want to change it:
tool_name_override="send_to_refund_team"

Now tool name:
send_to_refund_team()

3. tool_description_override
Tell to LLM:
when do we use this handsoff .

Example:
tool_description_override=
"Use this when customer wants money back"

### on_handoff callback

When handoff happend so if is there any extra work to do.

Example:
Before sending to Refund agent:

Save log into Database
Send Notification
Fetch Data

Example:
def on_handoff(ctx):
    print("Refund team activated")

Flow:
Triage Agent

     |
     ↓

on_handoff()

     |
     ↓

Refund Agent

### Handoff Inputs (input_type)
Sometime you want agents to provide extra information during handsoff

Example:
Customer:
"Double payment has been charged to me"

Triage agent:
While sending to refund agent:

{
 "reason": "duplicate_charge",
 "priority": "high"
}

### Real example with code 
"""
from pydantic import BaseModel


class EscalationData(BaseModel):
    reason: str


handoff_obj = handoff(
    agent=refund_agent,
    input_type=EscalationData
)
"""

Now:
LLM Call Handoff :
transfer_to_refund_agent
{reason:"duplicate_charge"}

### Input Filters 
When you dont want to let any agent to share any extra information while doing handsoff 
For removing tools call history : 
"""
from agents.extensions import handoff_filters


handoff(
    agent=refund_agent,
    input_filter=handoff_filters.remove_all_tools
)
"""

### Real world example of multiple handsoff

                 Banking Agent

                       |

       --------------------------------

       |              |               |

    Loan Agent   Card Agent    Transfer Agent