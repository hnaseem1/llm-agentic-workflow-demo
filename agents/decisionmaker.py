import os
from autogen_agentchat.agents import AssistantAgent

assignment = f"""
    You are the final decision maker. Your role is to:
      1. Make a final determination on scam probability
      2. Provide detailed explanation of the decision
      3. Provide a confidence level about your final determination in a scale from 1-5, where 5 is highly confident
"""

decision_maker = AssistantAgent(
            name="Decision_Maker",
            description="Synthesizes the analyses and make final determination",
            system_message=assignment,
            model_client=os.environ["MODEL"]
        )