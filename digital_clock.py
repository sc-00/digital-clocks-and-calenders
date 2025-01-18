import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.geometry("300x100")
root.title("digital clock- suling chu")
root.config(background = "black")

def clock():
    timeformat = strftime("%H:%M:%S")
    label.configure(text = timeformat)
    label.after(1000,clock)

label = Label(root,font = ("times new roman",50,"bold"),background = "black",foreground = "green")
label.pack()
clock()

root.mainloop()