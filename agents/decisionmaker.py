from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ChatCompletionClient

def decision_maker(model_client: ChatCompletionClient) -> AssistantAgent:
  assignment = f"""
      You are the final decision maker. Your role is to:
        1. Make a final determination on scam probability
        2. Provide detailed explanation of the decision
        3. Provide a confidence level about your final determination in a scale from 1-5, where 5 is highly confident
  """

  decision_maker_agent = AssistantAgent(
              name="Decision_Maker",
              description="Synthesizes the analyses and make final determination",
              system_message=assignment,
              model_client=model_client
          )
  
  return decision_maker_agent