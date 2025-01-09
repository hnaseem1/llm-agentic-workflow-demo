from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ChatCompletionClient

def summary_agent(model_client: ChatCompletionClient) -> AssistantAgent:
  assignment = f"""
      You are a communication specialist who creates clear, concise summaries of technical analyses. Your role is to:
        1. Synthesize the findings of a scam assessment into user-friendly language
        2. Highlight the most important points that users need to know
        3. Provide actionable recommendations
        4. Shorten your message into one paragraph
  """
  summary_agent = AssistantAgent(
              name="Summary_Agent",
              description="Generate a summary of the final determination",
              system_message=assignment,
              model_client=model_client
          )
  return summary_agent