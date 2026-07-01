from pathlib import Path
import sys

from agents import Agent, Runner

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.sdk_client import llm_model
from tools.main import weather_tool

AI_Assistant = Agent(
    name="AI_Assistant",
    instructions="You are a helpful AI Assistant. You will answer questions and provide information to the best of your ability.",
    model=llm_model,
    tools=[weather_tool],
)


def main():
    user_input = input("How can I help you today? ")
    result = Runner.run_sync(starting_agent=AI_Assistant, input=user_input)
    print(result.final_output)


if __name__ == "__main__":
    main()
