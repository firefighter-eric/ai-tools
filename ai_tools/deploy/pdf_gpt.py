import gradio as gr
from ai_tools.api.chatgpt import ChatGPTAPI


def process(api_key='', file=None) -> str:
    chatgpt = ChatGPTAPI(api_key)
    response = chatgpt(file)
    return 'Hello World!'


gr.Interface(fn=process, inputs=["text", "file"], outputs="text").launch()
