import tkinter as tk
from tkinter import messagebox


def show_reminder(text):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showwarning("地震速报", text)  # 弹出提醒窗口
    root.destroy()

