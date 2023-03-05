import gradio as gr
from ai_tools.api.chatgpt import ChatGPTAPI


def process(api_key='', user_input: str = '') -> str:
    chatgpt = ChatGPTAPI(api_key)
    gpt_output = chatgpt(user_input)
    return gpt_output


gr.Interface(fn=process, inputs=["text", "text"], outputs="text").launch()
