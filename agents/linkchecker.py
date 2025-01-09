from autogen_agentchat.agents import ToolUseAssistantAgent
from autogen_core.tools import FunctionTool
from tools.urlchecker import URLChecker
from autogen_core.models import ChatCompletionClient

def url_checker(model_client: ChatCompletionClient) -> ToolUseAssistantAgent:
    assignment = f"""
        You are a Link checker. Your role is to:
        1. Check the extracted text for any URLs
        2. Verify the legitimacy of the URLs using your registered function
    """
    url_checker = URLChecker()
    url_checker_tool = FunctionTool(
        url_checker.is_url_safe,
        description="Checks if a URL is safe"
    )
    url_checker_agent = ToolUseAssistantAgent(
                name="Link_Checker",
                description="Checks if a Link is safe",
                system_message=assignment,
                model_client=model_client,
                registered_tools=[url_checker_tool]
            )
    return url_checker_agent