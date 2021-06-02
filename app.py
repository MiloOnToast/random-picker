#Random name picker
#Author: Milo

import tkinter as tk
from tkinter import Button, Canvas, Entry, Label, Place, Tk, filedialog, Text
import os
from tkinter import font
import random
from tkinter.constants import BOTTOM, CENTER, TOP, X, Y

#main programme code
def randomize():
    names = entry.get().split(", " or ",")
    RandomName = (random.choice(names)).replace(",", "")
    print(RandomName)
    if RandomName == "":
        pastey.config(text=RandomName, bg="black")
    else:
        pastey.config(text=RandomName, bg="lightgrey")

#prettyness
root = Tk()
root.geometry("400x200")
root.configure(background="lightgrey")
root.title("Randomizer")

head = Label(root, text="Please enter names below...", bg="lightgrey", fg="Black", font=("Bahnschrift", 10))
head.place(x=50, y=10)

entry = Entry(root, width=40, font = ("Bahnschrift", 10))
entry.place(x=50, y=30)

clicky = Button(root, text="Click to randomize", bg="lightgrey", fg="black", font = ("Bahnschrift", 10), command = lambda: randomize())
clicky.place(x=130, y=90)

pastey = Label(root, text="", bg="lightgrey", fg="Black", font=("Bahnschrift", 10))
pastey.place(x=190, y=140)

root.mainloop()