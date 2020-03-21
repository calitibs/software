# class A:
#     pass
# a=A()
# a.name="gg"
# a.age=18
# #del a.age
# print(a.age)
#
# print(hasattr(a,"age"))   #一个实例手否存在该属性
# print(getattr(a,"age"))   #获取该实例的属性
# delattr(a,"age")          #删除某个属性
# setattr(a,"age",100)
# print(getattr(a,"age"))   #获取该实例的属性



'''
def hassttr(object,name_string):
    try:
        getattr(object,name_string)
        return True
    except AttributeError:
        return False
'''
# import requests
# from requests.exceptions import RequestException
# from tkinter import ttk
# import tkinter as tk
from PIL import Image
# import os.path
# root =  Tk()  # 初始化Tk()
# window = tk.Tk()  # 创建window窗口
# window.geometry("800x600")  # 设置窗口大小 注意：是x 不是
# window.title("利均成版特制翻译器")  # 定义窗口名称
# window.resizable(1, 1)  # 禁止调整窗口大小  0为不可变


# img = Image.open("图片1.jpg")
# width_org,height_org = img.size  # 查看原始图片大小
# print(width_org, height_org,img.size)
# a = 2  # 设置放大倍数
# width = int(width_org * a)
# height = int(height_org * a)

# print(width, height)
# new_img = img.resize((128, 128), Image.BILINEAR)  # 新图片的尺寸

# image_file = tk.PhotoImage(file='1.jpg')
# label_image = tk.Label(window, compound='center', image=image_file)

# tk.mainloop()

# img=Image.open("图片1.jpg")
# new_img=img.resize((128,128),Image.BILINEAR)
# new_img.save(self,"new_img.jpg")

im = Image.open('图片1.jpg')
im.save('test.png')