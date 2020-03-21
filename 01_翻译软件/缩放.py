import requests
from requests.exceptions import RequestException
from tkinter import ttk
import tkinter as tk
from PIL import Image

window = tk.Tk()  #创建window窗口
window.geometry("800x600")    # 设置窗口大小 注意：是x 不是
window.title("利均成特制版翻译器")  # 定义窗口名称
# window.resizable(1,1)  # 禁止调整窗口大小  0为不可变

input = tk.Entry(window, width=65,background = 'white')  # 创建一个输入框,并设置尺寸

input.place(x = 20, y = 35,input.pack(fill=tk.BOTH,expand=tk.YES))

tk.mainloop()

