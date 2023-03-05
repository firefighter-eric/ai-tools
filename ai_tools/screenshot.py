import tkinter as tk

import pyautogui
import pyscreenshot

# Get screen size, run to fix the size of the canvas
size = pyautogui.size()
# print(size)


def take_screenshot(image_path):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-alpha', 0.3)
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill='both', expand=True)

    rect = [0] * 4

    def show():
        canvas_h = canvas.winfo_screenheight()
        canvas_w = canvas.winfo_screenwidth()
        root_h = root.winfo_screenheight()
        root_w = root.winfo_screenwidth()
        print(canvas_h, canvas_w, root_h, root_w)

    def on_button_press(event):
        nonlocal rect
        rect = [event.x, event.y, event.x, event.y]

    def on_move_press(event):
        nonlocal rect
        canvas.delete('rect')
        rect = [rect[0], rect[1], event.x, event.y]
        canvas.create_rectangle(*rect, outline='red', tags='rect')

    def on_button_release(event):
        nonlocal rect

        root.destroy()

        if rect is not None:
            im = pyscreenshot.grab(bbox=rect)
            im.save(image_path)

    show()
    canvas.bind('<ButtonPress-1>', on_button_press)
    canvas.bind('<B1-Motion>', on_move_press)
    canvas.bind('<ButtonRelease-1>', on_button_release)

    root.mainloop()
    return rect


if __name__ == '__main__':
    r = take_screenshot('data/screenshot.png')
