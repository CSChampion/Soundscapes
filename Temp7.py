import tkinter as tk
from tkinter import *

#https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
#https://stackoverflow.com/questions/4246353/how-to-increase-the-font-size-of-a-text-widget

def input_mode():
    win1 = Tk()
    win1.geometry("250x150")
    win1.resizable(False, False)
    win1.title("Input Mode")

    def B2():
        global x
        x = 1
        win1.destroy()
    def B1():
        global x
        x = 0
        global file
        file = box1.get("1.0",'end-1c')
        win1.destroy()

    button1 = tk.Button(win1, text = "File", command = B1)
    button2 = tk.Button(win1, text = "Button", command = B2)
    box1 = tk.Text(win1, height=1, width=3, font=(16))
    button1.place(x = 76, y = 22)
    button2.place(x = 86, y = 75)
    box1.place(x = 131, y = 25)

    win1.mainloop()

def input_return():
    input_mode()
    if x == 1:
        return(1)
    elif x == 0:
        return(0)

def file_return():
    return(file)
