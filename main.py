from agents import Agent, Runner
from tools import config
import asyncio
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

waiter_agent = Agent(
    name = "Waiter Agent",
    instructions = """
    You are a waiter agent and provide a list of pizzas to the customer.
    ## Your pizza list:
    1. Malai Boti - $12
    2. Pepperoni - $14
    3. Fajita - $14
    """
)

welcome_agent = Agent(
    name = "Welcome Agent",  # Name corrected here
    instructions = RECOMMENDED_PROMPT_PREFIX + """
    You are a welcome agent in a Pizza Restaurant
    1. Welcome user politely.
    2. Ask them to have a seat.
    3. handoffs to the waiter agent to show the menu.""",
    handoffs = [waiter_agent]
)


async def main():
    while True:
        msg = input("Enter your message")
        result = await Runner.run(welcome_agent, msg, run_config = config)
        print(result.final_output)
        print(result.last_agent.name)
        
if __name__ == "__main__":
    asyncio.run(main())