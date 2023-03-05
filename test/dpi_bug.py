import tkinter as tk
import pyautogui

root1 = tk.Tk()

root_h = root1.winfo_screenheight()
root_w = root1.winfo_screenwidth()
print(root_h, root_w)

import pyautogui

size = pyautogui.size()
print(size)

root2 = tk.Tk()
root_h = root2.winfo_screenheight()
root_w = root2.winfo_screenwidth()
print(root_h, root_w)
