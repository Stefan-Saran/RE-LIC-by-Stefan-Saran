import tkinter as tk
import random
from random import randrange
from tkinter import *
from tkinter import messagebox
from getpass import getpass
import sys

app = tk.Tk()
app.configure(background='black')
HEIGHT = 400
WIDTH = 550


def generator(entry):
    for number in entry:
        if number == "+"or "*"or "!":
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            number = number.replace("*", str(randrange(10)))
            number2 = (number.replace("+", letter))
            number3 = (number2.replace("!", letter2))
            text_frame.insert(END,number3)
    text_frame.insert(END,"\n")

def delete():
    text_frame.delete(1.0,END)

canvas = tk.Canvas(app,width = WIDTH,height = HEIGHT,bg = "black")
canvas.pack()

frame = tk.Label(app,bg = "blue")
frame.place(rely = 0.020,relx = 0.5,relheight = 0.17,relwidth = 0.95,anchor = "n")

entry = tk.Entry(frame,bg = "#f0f0f0",bd = 4)
entry.place(rely = 0.15,relx = 0.025,relwidth = 0.36)

text_frame = tk.Text(app,fg = "black",bg = "#d1e7e8",wrap=WORD)
text_frame.place(rely = 0.23,relx = 0.05,relwidth=0.45, relheight=0.69)

text_frame2 = tk.Text(app,fg = "black",bg = "#d1e7e8",wrap=WORD,font = ("Times", 13))
text_frame2.place(rely = 0.23,relx = 0.52, relwidth=0.45, relheight=0.69)
text_frame2.config(state=DISABLED)

entry2 = tk.Entry(frame,bg = "#f0f0f0",bd = 4)
entry2.place(rely = 0.15,relx = 0.45,relwidth = 0.25)

button = tk.Button(frame,bg = "#e3e3e3",text = "Generate",fg = "black",bd = 4,font =("Times", 14),command = lambda: generator(entry.get()))
button.place(rely = 0.025, relx = 0.76,width = 100,height = 39,anchor = "w")

label = tk.Label(app,text = "|Pattern|", bg = "#a8a8a8",fg = "#000000",font=("Courier", 15))
label.place(rely = 0.12 ,relx = 0.1,height = 17)

label2 = tk.Label(app,text = "|Lines|",bg = "#a8a8a8",fg = "#000000",font=("Courier", 15))
label2.place(rely = 0.12,relx = 0.480 ,height = 17,anchor = "n")

app.mainloop()