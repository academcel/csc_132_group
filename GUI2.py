from tkinter import *
import random

def something():
    print("working code")

def opposite():
    i=10
    j=0
    while (j != i):
        t=1
        print(t)
        t +=1
        j +=1
        print(j)


window = Tk()
open = Button(window, text="Open", command=something)
close = Button(window, text="different", command=opposite)
open.pack()
close.pack()
window.mainloop()
