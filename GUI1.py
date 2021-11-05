import tkinter as tk
from tkinter import *

def cry():
    i=10
    while (i>0):
        i-=1
        print("tears falling down")
window = Tk()
open = Button(window, text="last")
close = Button(window, text="first", command=cry)
open.pack()
close.pack()
window.mainloop()
