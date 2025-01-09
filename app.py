from PIL import Image
import gradio as gr
from teams.scamdetection import ScamDetectorTeam
from tools.formatter import AutoGenFormatter


title = "ScamDetector: LLM Agents for Scam Protection"
description = """
              🦉 ScamDetector uses LLM Agents to analyze screenshots for potential scams. </br>

              🕵 LLM Agents coordinated as an AutoGen Team in a RoundRobin fashion: </br>
                - *OCR Specialist* </br>
                - *Link Checker* </br>
                - *Content Analyst* </br>
                - *Decision Maker* </br>
                - *Summary Specialist* </br>

              ♥️ Built with AutoGen 0.4.0 and OpenAI.  
              """
inputs = gr.components.Image()
outputs = [
    gr.components.Textbox(label="Analysis Result"),
    gr.HTML(label="Agentic Workflow (Streaming)")
]
examples = "examples"
example_labels = ["EN:Gift:Social", "ES:Banking:Social", "EN:Billing:SMS", "EN:Multifactor:Email", "EN:CustomerService:Twitter", "NO_TEXT:Landscape.HAM"]

agents = ScamDetectorTeam()
formatter = AutoGenFormatter()

def to_html(texts):
    formatted_html = ''
    for text in texts:
        formatted_html += text.replace('\n', '<br>') + '<br>'
    return f'<pre>{formatted_html}</pre>'

async def predict(img):
    try:
        img = Image.fromarray(img)
        stream = await agents.analyze(img)

        streams = []
        messages = []
        async for s in stream:
            streams.append(s)
            messages.append(await formatter.to_output(s))
            yield ["Pondering, stand by...", to_html(messages)]
        
        if streams[-1]:
            prediction = streams[-1].messages[-4].content
        else:
            prediction = "No analysis available. Try again later."

        await agents.reset()
        yield [prediction, to_html(messages)]

    except Exception as e:
        print(e)
        yield ["Error during analysis. Try again later.", ""]


with gr.Blocks() as demo:
    with gr.Tab("ScamDetector: AI Guardian for Scam Protection"):
        with gr.Row():
            gr.Interface(
                fn=predict,
                inputs=inputs,
                outputs=outputs,
                examples=examples,
                example_labels=example_labels,
                description=description,
            ).queue(default_concurrency_limit=5)

demo.launch()