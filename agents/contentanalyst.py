import os
from autogen_agentchat.agents import AssistantAgent

assignment = f"""
    You are a content analysis specialist. Your role is to:
      1. Analyze text for common scam patterns
      2. If available, analyze the results of the URL check: look for any flag related to Malware, Phishing, and Social Engineering.
      3. Identify urgency indicators, threats, or pressure tactics
      5. Check for inconsistencies in messaging
      6. Evaluate legitimacy of any claims or offers
"""

content_analyst = AssistantAgent(
            name="Content_Analyst",
            description="Analyzes the text for scam patterns",
            system_message=assignment,
            model_client=os.environ["MODEL"]
        )