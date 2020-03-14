import tkinter as tk
import random
from random import randrange
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.font as tkFont

app = tk.Tk()


def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("commands")

    l = tk.Label(win, bg="#343434", text="""
* = random number
+ = random lowercase letter
! = random uppercase letter""", height=15)
    l.grid(row=0, column=0)
    l.config(font=("Arial", 22))

    b = ttk.Button(win, text="Ok", command=win.destroy)
    b.grid(row=1, column=0)
    b.place(rely=0.9, relx=0.40)
    win.resizable(False, False)


Canvas = tk.Canvas(height=350, width=500, bg="#343434")
Canvas.pack(fill="both", expand=True)

Frame = tk.Frame(Canvas, height=350, width=500, bg="#343434")
Frame.pack(fill="both", expand=True)

label = tk.Label(Canvas, height=10, width=100, bg="#343434")
label.pack()

entry = tk.Entry(Frame, bg="#f0f0f0", bd=4, width=60)
entry.place(rely=0.3, relx=0.1,)

entry2 = tk.Entry(Frame, bg="#f0f0f0", bd=4, width=30)
entry2.place(rely=0.4, relx=0.1,)

Generate_button = tk.Button(
Frame, bg="#f0f0f0", command=lambda: generator(entry))
Generate_button.place(rely=0.7, relx=0.1, relwidth=0.3, relheight=0.09)
Generate_button.config(text="Generate")

Location_button = tk.Button(Frame, bg="#f0f0f0")
Location_button.place(rely=0.7, relx=0.6, relwidth=0.3, relheight=0.09)
Location_button.config(text="Output Location")

help_button = tk.Button(Frame, bg="#f0f0f0",
                        text="Show Info", command=popup_bonus)
help_button.place(rely=0.02, relx=0.02, relwidth=0.1, relheight=0.075)
help_button.config(text="Help")

app.mainloop()
