import random
from random import randrange
import tkinter as tk

pattern = input("Pattern: ")
line = int(input("Lines: "))


def generator():
    for number in pattern:
        if number == "+"or "*"or "!":
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            letter2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            number = number.replace("*", str(randrange(10)))
            number2 = (number.replace("+", letter))
            number3 = (number2.replace("!", letter2))
            print(str(number3), end="")
    print(end="\n")
    return str(generator())


def lines():
    for i in range(line):
        generator()


file1 = open("MyFile.txt", "a")
file1.write(generator())
file1.close()


lines()
