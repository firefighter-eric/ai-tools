from screenshot_gpt import ScreenShotGPT

screenshot_gpt = ScreenShotGPT()

while True:
    cmd = input('>>>')
    if cmd == 'q':
        break
    elif cmd == 's':
        resp = screenshot_gpt()
        print('gpt output:')
        print(resp)
        print('#' * 100, '\n' * 2)
