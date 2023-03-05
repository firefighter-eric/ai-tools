from api.chatgpt import ChatGPTAPI
from ocr.local_ocr import OCR
from screenshot import take_screenshot


class ScreenShotGPT:
    def __init__(self, openai_api_key: str = ''):
        self.chatgpt = ChatGPTAPI(api_key=openai_api_key)
        self.ocr = OCR()
        self.screenshot_path = 'data/screenshot.png'

    def __call__(self, output_flag=True):
        take_screenshot(self.screenshot_path)
        print('screenshot done')
        string = self.ocr(self.screenshot_path)
        print('ocr out:')
        print('-' * 100)
        print(string)
        print('-' * 100)

        response = self.chatgpt(string) if output_flag else ''
        return response


if __name__ == '__main__':
    screenshot_gpt = ScreenShotGPT()
    r = screenshot_gpt()
    print('gpt output:')
    print(r)
