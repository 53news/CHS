from tkinter import *

def start_main_gui():
    mw = Tk()
    mw.title("CHS test vision")                              #设置窗口名称
    winh = 250                                               #这里让窗口居中
    winw = 500
    scrh = mw.winfo_screenheight()                           # 修正函数名拼写错误
    scrw = mw.winfo_screenwidth()
    x = (scrw - winw)/2
    y = (scrh - winh)/2
    mw.geometry("%dx%d+%d+%d" %(winw,winh,x,y))                                   #设置窗口大小
    mw.configure(background="#8C92AC")
    mw.resizable(width=False, height=False)
    #********************窗口预设结束********************#
    label1 = Label(mw, text="CHShaking", font=("Arial", 22), fg="lightblue", bg="#8c92ac")
    label1.pack(side='top', fill='x')
    label2 = Label(mw, text="123456", font=("Arial", 18), fg="black", bg="#8c92ac")
    label2.pack(side='top', anchor='w')
    mw.mainloop()

