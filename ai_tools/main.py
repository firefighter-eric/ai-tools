from api.chatgpt import ChatGPTAPI
from ocr.local_ocr import OCR
from screenshot import take_screenshot


class ScreenShotGPT:
    def __init__(self):
        self.chatgpt = ChatGPTAPI()
        self.ocr = OCR()

    def __call__(self):
        take_screenshot('data/screenshot.png')
        print('screenshot done')
        string = self.ocr('data/screenshot.png')
        print('ocr out:')
        print('-' * 100)
        print(string)
        print('-' * 100)
        response = self.chatgpt(string)
        return response


if __name__ == '__main__':
    screenshot_gpt = ScreenShotGPT()
    r = screenshot_gpt()
    print(r)

# screenshot_gpt = ScreenShotGPT()
#
# while True:
#     cmd = input('>>>')
#     if cmd == 'q':
#         break
#     elif cmd == 's':
#         resp = screenshot_gpt()
#         print(resp)
