import openai


class ChatGPTAPI:
    def __init__(self, api_key=''):
        if not api_key:
            try:
                api_key = open('data/api_key.txt', 'r').read()
            except Exception as e:
                raise Exception(f'ChatGPT Error: No API key provided {e}')

        openai.api_key = api_key

    def __call__(self, content: str):
        assert isinstance(content, str), 'ChatGPT Error: content must be a string'
        content = content.strip()
        messages = [{'role': 'user', 'content': content}]
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            output: str = resp['choices'][0]['message']['content']
            output = output.strip()
        except Exception as e:
            raise Exception(f'ChatGPT Error: {e}')
        return output


if __name__ == '__main__':
    chatgpt = ChatGPTAPI()
    response = chatgpt('Hello, how are you?')
    print(response)
