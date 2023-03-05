import gradio as gr

from ai_tools.api.chatgpt import ChatGPTAPI
from ai_tools.utils.read_pdf import read_pdf


def process(api_key: str = '', prompt: str = '', file=None) -> str:
    chatgpt = ChatGPTAPI(api_key, max_input_length=1024)

    pdf_contents = read_pdf(file.name)
    pdf_str = '\n'.join(pdf_contents)
    content = prompt + '\n' + pdf_str
    response = chatgpt(content)
    return response


gr.Interface(fn=process, inputs=["text", "text", "file"], outputs="text").launch()
