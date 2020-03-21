import requests
from requests.exceptions import RequestException
from tkinter import ttk
import tkinter as tk
from PIL import Image

class Translate():
    def __init__(self):
        # root =  Tk()  # 初始化Tk()
        self.window = tk.Tk()  #创建window窗口
        self.window.geometry("800x600")    # 设置窗口大小 注意：是x 不是
        self.window.title("利均成特制版翻译器")  # 定义窗口名称
        self.window.resizable(0,0)  # 禁止调整窗口大小  0为不可变

        self.input = tk.Entry(self.window, width=65,background = 'white')  # 创建一个输入框,并设置尺寸
        self.info = tk.Text(self.window, width=65,height=10)   # 创建一个文本展示框，并设置尺寸

        # 添加一个按钮，用于触发翻译功能
        self.button=tk.Button(self.window,text='翻译',width='10',height=1,relief=tk.RAISED,background = 'white',command=self.translation)

        # 添加一个按钮，用于触发清空输入框功能
        self.button1 = tk.Button(self.window, text='清空输入', relief=tk.RAISED, width=10, height=1,background = 'white', command=self.clear_input)

        # # 添加一个按钮，用于触发清空输出框功能
        self.button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=10, height=1,background = 'white',command=self.clear_info)



        # 添加一张图标
        self.image_file = tk.PhotoImage(file='new_image.png')
        self.label_image = tk.Label(self.window,compound='center',image=self.image_file,background='black')


    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        # self.input.place(x = 20, y = 35)
        # self.info.place(x = 20, y = 60)
        # self.button.place(x = 490, y = 35)
        # self.button1.place(x=580, y=35)
        # self.button2.place(x=670, y=35)
        # self.label_image.place(x=480, y=60)

        self.input.pack(fill=tk.BOTH, expand=tk.YES)
        # self.info.pack(fill=tk.BOTH, expand=tk.YES)
        # self.button.pack(fill=tk.BOTH, expand=tk.YES)
        # self.button1.pack(fill=tk.BOTH, expand=tk.YES)
        # self.button2.pack(fill=tk.BOTH, expand=tk.YES)
        # self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        self.input.grid(row=0,sticky="W",padx=1)
        self.info.grid(row=1)
        self.button.grid(row=0,column=1,padx=2)
        self.button1.grid(row=0, column=2, padx=2)
        self.button2.grid(row=0,column=3,padx=2)
        self.label_image.grid(row=1, column=1,columnspan=3)


    def translation(self):
        """定义一个translation成翻译功能"""
        original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
        print(original_str)
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': original_str  # 将输入框输入的值，赋给接口参数
        }
        url = "http://fanyi.youdao.com/translate"
        try:
            r = requests.get(url, params=data)
            if r.status_code == 200:
                result = r.json()
                print(result)
                translate_result = result['translateResult'][0][0]["tgt"]
                print(translate_result)
                self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容
                self.info.insert('end',translate_result)  # 将翻译结果添加到输出框中
        except RequestException:
            self.info.insert('end', "发生错误")

    def clear_info(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(0.0,"end")  # 从第一行清除到最后一行

    def clear_input(self):
        """定义一个函数，用于清空输入框的内容"""
        self.input.delete(0,"end")

def main():

    # 修改图片尺寸
    img = Image.open('图片1.jpg')
    width, height = img.size
    # print(width, height)
    a = 0.8
    new_width = int(width * a)
    new_height = int(height * a)
    # print(new_width, new_height)
    out = img.resize((new_width, new_height), Image.BILINEAR)
    out.save('new_image.png')

    t=Translate()
    t.gui_arrang()
    tk.mainloop()
    input('input:')
if __name__ == '__main__':
    main()