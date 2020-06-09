modules = ["progressbar", "winshell"]

try:
    from tkinter.messagebox import showinfo
    from datetime import datetime
    from random import randrange
    from datetime import date
    from tkinter import ttk
    from time import sleep
    from tkinter import *
    import tkinter as tk
    import subprocess
    import traceback
    import textwrap
    import random
    import time
    import sys
    import os
    import tkinter.simpledialog
    from tkinter import messagebox
    import progressbar
    import winshell
except ImportError:
    import sys
    import pip
    import subprocess
    module_installation_question = input(
        "Some modules are missing, do you want to install all required modules for this project? yes or no.: ").lower()
    if module_installation_question == "yes":
        for module in modules:
            subprocess.call(['pip', 'install', module])
        print("Restart the editor and this project should work...")
        sys.exit()
    elif module_installation_question == "no":
        print("This project won't work if one module is missing...")
        sys.exit()


Lines_Generator = tk.Tk()

Lines_Generator.title("RE-LIC")
Lines_Generator.iconbitmap(r"Photos/logo.ico")
date = "Date: "

date_and_time_now = datetime.now()
date_format = date_and_time_now.strftime("%d.%m.%Y - %H.%M.%S")

filename = date_format + str(".txt")
saved_data_textfile_name = "Saved data from RE-LIC.txt"

Canvas = tk.Canvas(height=600, width=1000, bg="#343434")

Frame = tk.Frame(Canvas, height=600, width=1000, bg="#1A1A1A")

pattern_box = tk.Entry(Frame, bg="#F7F5EB",
                       font=('Verdana', 17), width=25)


lines_box = tk.Entry(Frame, bg="#F7F5EB", width=22, font=("Verdana", 13))


def string_to_integer():
    try:
        What_User_Wrote = lines_box.get()
        Convert_To_Int = int(What_User_Wrote)
        return Convert_To_Int
    except:
        tk.messagebox.showerror("Error", "Only Numbers allowed!")


def Generatung_lines2():
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
    completeName2.write('\n'.join(textwrap.wrap(a, d)))
    completeName2.close()


def Generating_lines1(entry, lines_counter):
    path_name = "Random lines generated"
    a = """"""
    c = 0
    d = len(entry.get())
    e = int(len(lines_box.get()))
    f = 0
    if not os.path.exists(path_name):
        os.makedirs(path_name)
        Generatung_lines2()
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
        completeName2.write('\n'.join(textwrap.wrap(a, d)))
        completeName2.close()

    command = '"{}" "{}" "{}"'.format(
        sys.executable,
        __file__,
        os.path.basename(__file__),
    )
    try:
        lines_counter.withdraw()
        createFolder()
        Lines_Generator.quit()
        subprocess.Popen(command)
    except Exception:
        lines_counter.deiconify()
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
    tk.Label(lines_counter,
             text="Generating, please wait it depends on number of lines...")

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(
        lines_counter, variable=progress_var, maximum=100)
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
        data_from_user()


def data_from_user():
    pattern_box_get = pattern_box.get()
    lines_box_get = lines_box.get()
    saved_data_text = f"{pattern_box_get}\n{lines_box_get}"
    saved_data = open(saved_data_textfile_name, "w+")
    saved_data.seek(0)
    saved_data.truncate(0)
    saved_data.write(saved_data_text)
    saved_data.close()


def warning():
    a = len(pattern_box.get())
    b = len(lines_box.get())
    if pattern_box.get() == entry1_text and lines_box.get() == lines_box_text or a == 0 and b == 0 or a == 0 and lines_box.get() == lines_box_text or b == 0 and pattern_box.get() == entry1_text:
        messagebox.showerror("Error", "The boxes cannot be blank!")
    elif lines_box.get() == lines_box_text and a >= 0 or a >= 0 and b == 0:
        messagebox.showerror("Error", "Line Box cannot be blank!")
    elif pattern_box.get() == entry1_text and b >= 0 or b >= 0 and a == 0:
        messagebox.showerror("Error", "Pattern Box cannot be blank!")
    elif string_to_integer() > 10000:
        messagebox.showinfo("Error", "The maximum number of lines is 10.000!")
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
    width = 300
    height = 400
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
    width = 300
    height = 400
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
    if pattern_box.get() == entry1_text:
        pattern_box.delete(0, END)
        pattern_box.configure(foreground="black")
    elif len(pattern_box.get()) != entry1_text:
        pattern_box.configure(foreground="black")
    else:
        pass


def clear_lines_box(event2):
    if lines_box.get() == lines_box_text:
        lines_box.delete(0, END)
        lines_box.configure(foreground="black")
    else:
        pass


entry1_text = "Enter your code pattern here"
lines_box_text = "How many lines?"


def text_effect(asd1):
    if len(pattern_box.get()) == 0 and len(lines_box.get()) == 0:
        pattern_box.insert(0, "Enter your code pattern here")
        lines_box.insert(0, "How many lines?")
        pattern_box.configure(foreground="gray")
        lines_box.configure(foreground="gray")
        Lines_Generator.focus()
    elif len(pattern_box.get()) == 0:
        pattern_box.insert(0, "Enter your code pattern here")
        pattern_box.configure(foreground="gray")
        Lines_Generator.focus()
    elif len(lines_box.get()) == 0:
        lines_box.insert(0, "How many lines?")
        lines_box.configure(foreground="gray")
        Lines_Generator.focus()
    else:
        pass


def saved_data_from_relic():
    if os.path.exists(saved_data_textfile_name):
        open_textfile = open(saved_data_textfile_name)
        lines = open_textfile.read().splitlines()
        try:
            asd = lines[0]
            asd1 = lines[1]
            pattern_box.delete(0, END)
            lines_box.delete(0, END)
            pattern_box.insert(0, asd)
            lines_box.insert(0, asd1)
            open_textfile.close()
        except:
            tk.messagebox.showerror("Error", "Something went wrong...")


saved_data_from_relic()
generate_button_font = ('Arial', 12)
help_button_font = ("Arial", 10)
about_button_font = ("Arial", 10)


Generate_button = tk.Button(
    Frame, bg="#f0f0f0", font=generate_button_font, foreground="#2b2b2b", command=lambda: warning())


help_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                        foreground="#2b2b2b", command=Help_window)


about_button = tk.Button(Frame, bg="#F7F5EB", font=help_button_font,
                         foreground="#2b2b2b", command=About_window)

if len(lines_box.get()) == 0 and len(pattern_box.get()) == 0:
    lines_box.insert(0, lines_box_text)
    pattern_box.insert(0, entry1_text)
    pattern_box.configure(foreground="gray")
    lines_box.configure(foreground="gray")
else:
    pass

Canvas.pack(fill="both", expand=True)
Frame.pack(fill="both", expand=True)
pattern_box.place(relx=0.5, rely=0.3, anchor="center")
lines_box.place(relx=0.5, rely=0.5, anchor="center")
Generate_button.place(rely=0.7, relx=0.35, relwidth=0.31, relheight=0.12)
help_button.place(rely=0.03, relx=0.88, relwidth=0.1, relheight=0.075)
about_button.place(rely=0.03, relx=0.02, relwidth=0.1, relheight=0.075)


Generate_button.config(text="Generate")
help_button.config(text="Help")
about_button.config(text="About")

center_window(600, 350)
Lines_Generator.minsize(390, 200)
Lines_Generator.geometry("500x300")

help_button.bind("<Button-1>", text_effect)
Generate_button.bind("<Button-1>", text_effect)
about_button.bind("<Button-1>", text_effect)
Frame.bind("<Button-1>", text_effect)
pattern_box.bind("<Button-1>", clearn_code_pattern)
lines_box.bind("<Button-1>", clear_lines_box)

if pattern_box.get() == entry1_text:
    pattern_box.configure(foreground="gray")
else:
    pattern_box.configure(foreground="black")

Lines_Generator.mainloop()
