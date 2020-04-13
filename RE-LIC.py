from pip._vendor.progress.bar import PixelBar
from pip._vendor.progress.bar import Bar
from tkinter.messagebox import showinfo
from datetime import datetime
import tkinter.font as tkFont
from random import randrange
from datetime import date
from tkinter import ttk
from time import sleep
from tkinter import *
import tkinter as tk
import subprocess
import traceback
import textwrap
import pickle
import random
import time
import sys
import os
import tkinter.simpledialog
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
from tkinter import colorchooser
import progressbar

app = tk.Tk()

app.title("RE-LIC")
app.iconbitmap(r"Photos/logo.ico")
date = "Date: "

today1 = datetime.now()
d2 = today1.strftime("%d.%m.%Y - %H.%M.%S")

filename = d2 + str(".txt")


def line():
    What_User_Wrote = entry2.get()
    Convert_To_Int = int(What_User_Wrote)
    return Convert_To_Int


# def popup_no_code_pattern():
    #d = len(entry.get())
    #e = int(len(entry2.get()))
    # if e and d == 0:
    # return SystemExit

def generator(entry, popup):
    path_name = "Random codes generated"
    a = """"""
    c = 0
    d = len(entry.get())
    e = int(len(entry2.get()))
    f = 0
    if not os.path.exists(path_name):
        os.makedirs(path_name)
    else:
        completeName2 = os.path.join(path_name, filename+".txt")
        completeName2 = open(completeName2, "w")
        for i in range(line()):
            for number in entry.get():
                if number == "+"or "*"or "!":
                    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
                    letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    number = number.replace("*", str(randrange(10)))
                    number2 = (number.replace("+", letter))
                    number3 = (number2.replace("!", letter2))
                    a = a + (str(number3))
            popup.title("Writing lines...")
        completeName2.write('\n'.join(textwrap.wrap(a, d)))
        completeName2.close()

    command = '"{}" "{}" "{}"'.format(
        sys.executable,
        __file__,
        os.path.basename(__file__),
    )
    try:
        createFolder()
        app.quit()
        subprocess.Popen(command)
    except Exception:
        traceback.print_exc()
        sys.exit('fatal error occurred rerunning script')
    else:
        pass


def createFolder(directory="Pattern and lines(saved data)"):
    b = str(entry.get())
    c = str(entry2.get())
    q = f"{b}" + "\n"
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            completeName = os.path.join(
                directory, filename+"(Pattern and Lines)"+".txt")
            directory1 = open(completeName, "w")
            directory1.write(str(q+c))
            directory1.close()
    except OSError:
        messagebox.showerror("Error", "Creating directory" + directory)


def button_command():
    teams = range(line())
    # start progress bar
    popup = tk.Toplevel(background="#1A1A1A")
    popup.config(menu="")
    popup.title("Generating...")
    tk.Label(popup, text="Generating, please wait it depends on number of lines...")

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=100)
    progress_bar.place(rely=0.25, relx=0.05, relwidth=0.9)
    popup.pack_slaves()

    label_button_command = tk.Label()

    progress_step = float(100.0/len(teams))
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    width2 = 270
    height2 = 50
    x = (screen_width/2) - (width2/2)
    y = (screen_height/2) - (height2/2)
    popup.geometry('%dx%d+%d+%d' % (width2, height2, x, y))

    for team in teams:
        popup.update()
        progress += progress_step
        progress_var.set(progress)
    popup.resizable(False, False)
    popup.after(0, generator(entry, popup))
    return 0


def test():
    if not entry2.get().isdigit():
        showinfo("Error", "line box should only contain numbers!")
    else:
        button_command()


def warning():
    a = len(entry.get())
    b = len(entry2.get())
    c = "Enter your code pattern here"
    d = "How many lines?"
    if entry.get() == c and entry2.get() == d or a == 0 and b == 0 or a == 0 and entry2.get() == d or b == 0 and entry.get() == c:
        messagebox.showerror("Error", "The boxes cannot be blank!")
    elif entry2.get() == d and a >= 0 or a >= 0 and b == 0:
        messagebox.showerror("Error", "Line Box cannot be blank!")
    elif entry.get() == c and b >= 0 or b >= 0 and a == 0:
        messagebox.showerror("Error", "Pattern Box cannot be blank!")
    elif line() > 50000:
        messagebox.showinfo("Error", "The maximum number of lines is 50.000!")
    else:
        test()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))


def popup_bonus():
    root = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 14)
    root.title("Commands")
    w = 300     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = """\n\n\n\n\n\n
* = random number
+ = random lowercase letter
! = random uppercase letter

    """
    m += '\n'
    w = Label(root, text=m, width=120, height=10,
              background="#1A1A1A", foreground="white", font=large_font2)
    w.pack()

    root.transient(app)
    root.grab_set()
    root.wait_window(root)

    root.resizable(False, False)
    root.mainloop()


def popup_bonus2():
    today = datetime.now()
    a = "This is RE-LIC"
    bolded_string = "\033[1m" + a + "\033[0m"
    root = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 13)
    root.title("About")
    w = 300     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = f"""


|{a}|
---------------------------
\nThis program uses characters to \ngenerate new lines with random\n letters and numbers.\nCertain letters\n can also be specified\n
---------------------------
Creator = Stefan Saran
---------------------------

---------------------------
Creation date started: 
November 10th. 2019
---------------------------
"""
    m += '\n'
    w = Label(root, text=m, width=120, height=18,
              background="#1A1A1A", foreground="white", font=large_font2)
    w.pack()

    root.transient(app)
    root.grab_set()
    root.wait_window(root)

    root.resizable(False, False)
    root.mainloop()


def clear_search(event):
    if len(entry.get()) <= 0:
        pass
    elif entry.get() == "Enter your code pattern here":
        entry.delete(0, END)


def clear_search2(event2):
    if len(entry2.get()) <= 0:
        pass
    elif entry2.get() == "How many lines?":
        entry2.delete(0, END)


Canvas = tk.Canvas(height=600, width=1000, bg="#343434")
Canvas.pack(fill="both", expand=True)

Frame = tk.Frame(Canvas, height=600, width=1000, bg="#1A1A1A")
Frame.pack(fill="both", expand=True)

large_font = ('Verdana', 17)
entry = tk.Entry(Frame, bg="#F7F5EB", font=large_font, width=25)
entry.place(rely=0.3, relx=0.17)
a = "Enter your code pattern here"
entry.insert(0, a)
entry.configure(foreground="gray")
entry.bind("<Button-1>", clear_search)

# while len(entry.get()) < 0:
#entry.insert(0, "Enter your code pattern here")
# while len(entry) > 0:
#entry.delete(0, "end")

entry2 = tk.Entry(Frame, bg="#F7F5EB", width=22, font=("Verdana", 11))
entry2.pack(expand=True)
b = "How many lines?"
entry2.insert(0, b)
entry2.configure(foreground="gray")
entry2.bind("<Button-1>", clear_search2)

generate_button_font = ('Arial', 12)
Generate_button = tk.Button(
    Frame, bg="#f0f0f0", font=generate_button_font, foreground="#525252", command=lambda: warning())
Generate_button.pack()
Generate_button.place(rely=0.7, relx=0.35, relwidth=0.31, relheight=0.12)
Generate_button.config(text="Generate")

help_button_font = ("Arial", 10)
help_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                        foreground="#525252", command=popup_bonus)
help_button.place(rely=0.03, relx=0.88, relwidth=0.1, relheight=0.075)
help_button.config(text="Help")

about_button_font = ("Arial", 10)
about_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                         foreground="#525252", command=popup_bonus2)
about_button.place(rely=0.03, relx=0.02, relwidth=0.1, relheight=0.075)
about_button.config(text="About")

center_window(600, 350)

app.mainloop()
