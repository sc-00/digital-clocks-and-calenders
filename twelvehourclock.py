import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.geometry("375x100")
root.title("digital clock- suling chu")
root.config(background = "black")

def clock():
    timeformat = strftime("%I:%M:%S %p")
    label.configure(text = timeformat)
    label.after(1000,clock)

label = Label(root,font = ("times new roman",50,"bold"),background = "black",foreground = "lime")
label.pack()
clock()

root.mainloop()