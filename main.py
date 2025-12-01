import tkinter
from tkinter import *

root = tkinter.Tk()

root.title("Fist Project")
root.geometry("640x480")
root.iconbitmap("icon.ico")

label1 = Label(text = "Hello World!!!")
label1.pack()

root.mainloop()