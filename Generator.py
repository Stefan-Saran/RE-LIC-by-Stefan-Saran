import tkinter as tk
import random
from random import randrange
from tkinter import *
from tkinter import messagebox
import time

app = tk.Tk()
HEIGHT = 400
WIDTH  = 550
#def line_counter():
    #count = text_frame.option_readfile(text_frame)
    #return count

list1 =f"""Ctrl + a = select all
Ctrl + c = copy selected text
Ctrl + v = paste
------------------------------------
(*) = random number
(+) = random letter (lowercase)
(!) = random letter (uppercase)
"""

#def delete_count():
    #text_frame2.delete()



#def count():
    #count = []
    #teext = int(text_frame.index('end-1c').split(".")[0])
    #teext = str(teext - 1)
    #count+=teext
    #for line in text_frame:
        #if len(line) == 0:
            #line.delete()
            #text_frame2.insert(1.12,count)


def generator(entry):
    for number in entry:
        if number == "x"or "*"or "!":
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            number = number.replace("*", str(randrange(10)))
            number2 = (number.replace("+", letter))
            number3 = (number2.replace("!", letter2))
            text_frame.insert(END, number3)
    text_frame.insert(END, "\n")


def linesa(entry2):
    what_user_wrote = entry2.get()
    line = int(what_user_wrote)
    for i in range(line):
        generator(entry)


def delete():
    text_frame.delete(1.0,END)
    #delete_count()
    #text_frame2.insert(1.12,"0")

#image = tk.PhotoImage(file = "683980.png")
canvas = tk.Canvas(height = 500, width = 850,bg="black")
canvas.pack()
app.configure(background='black')

#frame3 = tk.Label(app,image = image)
#frame3.place(width = 500,height = 400)

frame = tk.Label(canvas,bg = "blue")
frame.place(rely = 0.020,relx = 0.5,relheight = 0.19,relwidth = 0.95,anchor = "n")

#scrollbar2 = Scrollbar(frame3)
#scrollbar2.pack(side=RIGHT, fill=Y)

entry = tk.Entry(frame,bg = "#f0f0f0",bd = 4)
entry.place(rely = 0.15,relx = 0.025,relwidth = 0.36)

#scrollbar = Scrollbar(frame2)
#scrollbar.pack(side=RIGHT, fill=Y)

text_frame = tk.Text(app,fg = "black",bg = "#d1e7e8",wrap=WORD)
text_frame.place(rely = 0.23,relx = 0.05,relwidth=0.45, relheight=0.69)
#scrollbar.config(command=text_frame.yview)

text_frame2 = tk.Text(app,fg = "black",bg = "#ebedeb",wrap=WORD,font = ("Times", 13))
text_frame2.place(rely = 0.23,relx = 0.52, relwidth=0.45, relheight=0.69)
text_frame2.insert(END,list1)
#scrollbar2.config(command=text_frame2.yview)
text_frame2.config(state=DISABLED)

entry2 = tk.Entry(frame,bg = "#f0f0f0",bd = 4)
entry2.place(rely = 0.15,relx = 0.45,relwidth = 0.25)

button2 = tk.Button(frame,bg = "#e3e3e3",text = "Clear textbox",font =("Times",13),command = delete)
button2.place(rely = 0.61,relx = 0.75,width = 110,height = 28)

button = tk.Button(frame,bg = "#e3e3e3",text = "Generate",fg = "black",bd = 4,font =("Times", 14),command = lambda: linesa(entry2))
button.place(rely = 0.025, relx = 0.76,width = 100,height = 39,anchor = "w")

label = tk.Label(frame,text = "|Pattern|", bg = "#a8a8a8",fg = "#000000",font=("Courier", 15))
label.place(rely = 0.59,relx = 0.026,relheight = 0.28,anchor = "w")

label2 = tk.Label(frame,text = "|Lines|",bg = "#a8a8a8",fg = "#000000",font=("Courier", 15))
label2.place(rely = 0.45,relx = 0.451 ,relheight = 0.28)
app.mainloop()
