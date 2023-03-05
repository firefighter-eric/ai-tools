import openai
import tiktoken


class ChatGPTAPI:
    def __init__(self, api_key='', max_input_length=1024):
        if not api_key:
            try:
                api_key = open('data/api_key.txt', 'r').read()
            except Exception as e:
                raise Exception(f'ChatGPT Error: No API key provided {e}')

        openai.api_key = api_key
        self.max_input_length = max_input_length
        self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    def truncate_string(self, s):
        e = self.encoding.encode(s)[:self.max_input_length]
        s = self.encoding.decode(e)
        return s

    def __call__(self, content: str):
        assert isinstance(content, str), 'ChatGPT Error: content must be a string'
        content = content.strip()
        content = self.truncate_string(content)
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
    r = chatgpt.truncate_string('how are you ' * 10000)
    r_list = r.split(' ')
    # response = chatgpt('Hello, how are you?')
    # print(response)
