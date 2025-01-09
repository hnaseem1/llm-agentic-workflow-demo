from typing import List, AsyncIterator
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core import Image as AGImage
from PIL import Image
from autogen_agentchat.agents import AssistantAgent
from agents.ocrspecialist import ocr_specialist
from agents.linkchecker import url_checker
from agents.contentanalyst import content_analyst
from agents.decisionmaker import decision_maker
from agents.summaryagent import summary_agent

class ScamDetectorTeam:
    """
    ScamDetector Team tasked with Scam Protection using an Agentic Workflow
    """

    def __init__(self):
        """
        Initialize ScamDetector with agents and tools
        """
        self.agents = self.create_agents()
        self.team = self.create_team()

    def create_agents(self) -> List[AssistantAgent]:
        """Create all required agents with their specialized roles and tools"""
        agents = [ocr_specialist, url_checker, content_analyst, decision_maker, summary_agent]
        return agents
    
    def create_team(self) -> RoundRobinGroupChat:
        """Create a team of agents that work together in Round Robin fashion"""
        termination = TextMentionTermination("NO_TEXT_FOUND")

        return RoundRobinGroupChat(
            self.agents,
            max_turns=7,
            termination_condition=termination
        )
    
    async def reset(self):
        """Reset team state"""
        await self.team.reset()

    async def analyze(self, image: Image) -> AsyncIterator:
        """
        Analyze an image for potential scams.
        """
        img = AGImage(image)
        mm_message = MultiModalMessage(content=[img], source="User")

        return self.team.run_stream(task=mm_message)
    
    