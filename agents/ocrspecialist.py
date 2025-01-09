import os
from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from tools.imageocr import ImageOCR

assignment = f"""
    You are an OCR specialist. Your role is to:
      1. Extract text from an image using Optical Character Recognition (OCR)
      2. Clean and format the extracted text
      3. Do not perform any analysis on the extracted text
      4. Reply with the extracted text
      5. If there is no text in the image, reply with "NO_TEXT_FOUND"
"""

ocr = ImageOCR()
ocr_tool = FunctionTool(
    ocr.extract_text,
    description="Extracts text from an image path"
)

ocr_specialist = AssistantAgent(
            name="OCR_Specialist",
            description="Extracts text from an image",
            system_message=assignment,
            model_client=os.environ["MODEL"],
            tools=[ocr_tool]
        )