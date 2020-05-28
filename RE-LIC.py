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

Lines_Generator = tk.Tk()

Lines_Generator.title("RE-LIC")
Lines_Generator.iconbitmap(r"Photos/logo.ico")
date = "Date: "

date_and_time_now = datetime.now()
date_format = date_and_time_now.strftime("%d.%m.%Y - %H.%M.%S")

filename = date_format + str(".txt")


def string_to_integer():
    What_User_Wrote = lines_box.get()
    Convert_To_Int = int(What_User_Wrote)
    return Convert_To_Int


def Generatung_lines2(popup):
    path_name = "Random lines generated"
    a = """"""
    c = 0
    d = len(pattern_box.get())
    e = int(len(lines_box.get()))
    f = 0
    completeName2 = os.path.join(path_name, filename+".txt")
    completeName2 = open(completeName2, "w")
    for i in range(string_to_integer()):
        for number in pattern_box.get():
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


def Generating_lines1(entry, popup):
    path_name = "Random lines generated"
    a = """"""
    c = 0
    d = len(entry.get())
    e = int(len(lines_box.get()))
    f = 0
    if not os.path.exists(path_name):
        os.makedirs(path_name)
        Generatung_lines2(popup)
    else:
        completeName2 = os.path.join(path_name, filename+".txt")
        completeName2 = open(completeName2, "w")
        for i in range(string_to_integer()):
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
        Lines_Generator.quit()
        subprocess.Popen(command)
    except Exception:
        traceback.print_exc()
        sys.exit('fatal error occurred rerunning script')
    else:
        pass


def createFolder(directory="Pattern and lines(saved data)"):
    b = str(pattern_box.get())
    c = str(lines_box.get())
    q = f"{b}" + "\n"
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            completeName = os.path.join(
                directory, filename+"(Pattern and Lines)"+".txt")
            directory1 = open(completeName, "w")
            directory1.write(str(q+c))
            directory1.close()
        else:
            completeName = os.path.join(
                directory, filename+"(Pattern and Lines)"+".txt")
            directory1 = open(completeName, "w")
            directory1.write(str(q+c))
            directory1.close()
    except OSError:
        messagebox.showerror("Error", "Creating directory" + directory)


def Lines_generating_time():
    lines_count = range(string_to_integer())
    # start progress bar
    lines_counter = tk.Toplevel(background="#303030")
    lines_counter.attributes('-topmost', 'true')
    lines_counter.wm_overrideredirect(True)
    lines_counter.config(menu="")
    lines_counter.title("Generating...")
    tk.Label(lines_counter, text="Generating, please wait it depends on number of lines...")

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(lines_counter, variable=progress_var, maximum=100)
    progress_bar.place(rely=0.25, relx=0.05, relwidth=0.9)
    lines_counter.pack_slaves()

    label_button_command = tk.Label()

    progress_step = float(100.0/len(lines_count))
    screen_width = lines_counter.winfo_screenwidth()
    screen_height = lines_counter.winfo_screenheight()

    width2 = 270
    height2 = 50
    x = (screen_width/2) - (width2/2)
    y = (screen_height/2) - (height2/2)
    lines_counter.geometry('%dx%d+%d+%d' % (width2, height2, x, y))

    for team in lines_count:
        lines_counter.update()
        progress += progress_step
        progress_var.set(progress)
    lines_counter.resizable(False, False)
    lines_counter.after(0, Generating_lines1(pattern_box, lines_counter))
    return 0


def disabling_and_warning():
    Lines_Generator.withdraw()
    if not lines_box.get().isdigit():
        showinfo("Error", "line box should only contain numbers!")
    else:
        Lines_generating_time()


def warning():
    a = len(pattern_box.get())
    b = len(lines_box.get())
    c = "Enter your code pattern here"
    d = "How many lines?"
    if pattern_box.get() == c and lines_box.get() == d or a == 0 and b == 0 or a == 0 and lines_box.get() == d or b == 0 and pattern_box.get() == c:
        messagebox.showerror("Error", "The boxes cannot be blank!")
    elif lines_box.get() == d and a >= 0 or a >= 0 and b == 0:
        messagebox.showerror("Error", "Line Box cannot be blank!")
    elif pattern_box.get() == c and b >= 0 or b >= 0 and a == 0:
        messagebox.showerror("Error", "Pattern Box cannot be blank!")
    elif string_to_integer() > 50000:
        messagebox.showinfo("Error", "The maximum number of lines is 50.000!")
    else:
        disabling_and_warning()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = Lines_Generator.winfo_screenwidth()
    screen_height = Lines_Generator.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Lines_Generator.geometry('%dx%d+%d+%d' % (width, height, x, y))


def Help_window():
    help = Toplevel(background="#1A1A1A")
    large_font2 = ('Verdana', 14)
    help.title("Commands")
    width = 300     # popup window width
    height = 400     # popup window height
    screenwidth = help.winfo_screenwidth()
    screenheight = help.winfo_screenheight()
    x = (screenwidth - width)/2
    y = (screenheight - height)/2
    help.geometry('%dx%d+%d+%d' % (width, height, x, y))
    help_info = """\n\n\n\n\n\n
* = random number
+ = random lowercase letter
! = random uppercase letter
    """
    help_info += '\n'
    width = Label(help, text=help_info, width=120, height=10,
              background="#1A1A1A", foreground="white", font=large_font2)
    width.pack()

    help.transient(Lines_Generator)
    help.grab_set()
    help.wait_window(help)
    try:
        help.resizable(False, False)
    except TclError:
        pass
    help.mainloop()


def About_window():
    today = datetime.now()
    title = "This is RE-LIC"
    bolded_string = "\033[1m" + title + "\033[0m"
    About = Toplevel(background="#1A1A1A")
    help_font = ('Verdana', 13)
    About.title("About")
    width = 300     # popup window width
    height = 400     # popup window height
    screenwidth = About.winfo_screenwidth()
    screenheight = About.winfo_screenheight()
    x = (screenwidth - width)/2
    y = (screenheight - height)/2
    release_date = str("November 10th. 2019 - May 8th. 2020")
    About.geometry('%dx%d+%d+%d' % (width, height, x, y))
    about_info = f"""
|{title}|
---------------------------
\nThis program uses characters to \ngenerate new lines with random\n letters and numbers.\nCertain letters\n can also be specified\n
---------------------------
Creator = Stefan Saran
---------------------------
---------------------------
Creation date: 
---------------------------
"""
    about_info += '\n'
    width = Label(About, text=about_info, width=120, height=18,
              background="#1A1A1A", foreground="white", font=help_font)
    width.pack()

    release_date2 = tk.Label(width, text=release_date,
                             background="#1A1A1A", foreground="white")
    release_date2.place(rely=0.92, relx=0.5, anchor="center")
    release_date2["font"] = 10

    About.transient(Lines_Generator)
    About.grab_set()
    About.wait_window(About)
    try:
        About.resizable(False, False)
    except TclError:
        pass
    About.mainloop()


def clearn_code_pattern(event):
    if pattern_box.get() == "Enter your code pattern here":
        pattern_box.delete(0, END)


def clear_lines_box(event2):
    if lines_box.get() == "How many lines?":
        lines_box.delete(0, END)


def insert_entry1_text(asd1):
    if len(pattern_box.get()) == 0:
        pattern_box.insert(0, "Enter your code pattern here")
    else:
        pass


def insert_entry2_text(asd2):
    if len(lines_box.get()) == 0:
        lines_box.insert(0, "How many lines?")
    elif lines_box.get() == "How many lines?":
        lines_box.delete(0, END)


Canvas = tk.Canvas(height=600, width=1000, bg="#343434")
Canvas.pack(fill="both", expand=True)

Frame = tk.Frame(Canvas, height=600, width=1000, bg="#1A1A1A")
Frame.pack(fill="both", expand=True)

large_font = ('Verdana', 17)
pattern_box = tk.Entry(Frame, state=NORMAL, bg="#F7F5EB",
                 font=large_font, width=25)
pattern_box.place(relx=0.5, rely=0.3, anchor="center")
entry1_text = "Enter your code pattern here"
pattern_box.insert(0, entry1_text)
pattern_box.configure(foreground="gray")
pattern_box.bind("<Button-1>", clearn_code_pattern)

lines_box = tk.Entry(Frame, bg="#F7F5EB", width=22, font=("Verdana", 11))
lines_box.place(relx=0.5, rely=0.5, anchor="center")
b = "How many lines?"
lines_box.insert(0, b)
lines_box.configure(foreground="gray")
lines_box.bind("<Button-1>", clear_lines_box)

generate_button_font = ('Arial', 12)
Generate_button = tk.Button(
    Frame, bg="#f0f0f0", font=generate_button_font, foreground="#525252", command=lambda: warning())
Generate_button.place(rely=0.7, relx=0.35, relwidth=0.31, relheight=0.12)
Generate_button.config(text="Generate")

help_button_font = ("Arial", 10)
help_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                        foreground="#525252", command=Help_window)
help_button.place(rely=0.03, relx=0.88, relwidth=0.1, relheight=0.075)
help_button.config(text="Help")

about_button_font = ("Arial", 10)
about_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                         foreground="#525252", command=About_window)
about_button.place(rely=0.03, relx=0.02, relwidth=0.1, relheight=0.075)
about_button.config(text="About")

center_window(600, 350)
Lines_Generator.minsize(390, 200)
Lines_Generator.geometry("500x300")

Lines_Generator.mainloop()
