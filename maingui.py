# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
############UUUSEE THIS ONE###########

from tkinter import *
from tkinter.ttk import *
#from motor import motorL, motorR

# creates a Tk() object
def mainScreen():
    global master
    master = Tk()

    # sets the geometry of main
    # root window
    master.geometry("300x300")
    label = Label(master, text="This is the main window")
    label.pack(pady=10)

    # a button widget which will open a
    # new window on button click
    bot1 = Button(master, text="Click to open Light controls.", command=windowTwo)
    bot2 = Button(master, text="Click to open Motor controls.", command=windowThree)
    bot3 = Button(master, text="Click to open watering system controls.", command=windowFour)
    bot1.pack(pady=3)
    bot2.pack(pady=2)
    bot3.pack(pady=1)

    # mainloop, runs infinitely
    mainloop()

# function to open a new window
# on a button click
def windowTwo():
    # Toplevel object which will
    # be treated as a new window
    master.withdraw()
    window2 = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    window2.title("Module 1")

    # sets the geometry of toplevel
    window2.geometry("300x300")

    # A Label widget to show in toplevel
    Label(window2, text="Light switch controls.")
    bot1 = Button(window2, text="Toggle the lights.")  #command=pass#)
    bot2 = Button(window2, text ="Go back to the main menu.", command=inbetween)
    bot1.pack(pady=20)
    bot2.pack(pady=10)

def windowThree():
    master.withdraw()
    window3 = Toplevel(master)
    window3.title("Module 2")
    window3.geometry("300x300")
    note = Label(window3, text="The motor can open or close the curtain.", )
    #bot1 = Button(window3, text="Open the curtain", command=motorR)
    #bot2 = Button(window3, text="Close the curtain", command=motorL)
    bot3 = Button(window3, text="Go back to the main menu.", command=inbetween)
    note.pack(expand=1)
    #bot1.pack
    #bot2.pack
    bot3.pack(pady=10)

def windowFour():
    master.withdraw()
    window4 = Toplevel(master)
    window4.title("Module 3")
    window4.geometry("400x400")
    note = Label(window4, text="Control when plant is watered, and if the plant gets water.")
    bot3 = Button(window4, text="Go back to the main menu.", command=inbetween)
    note.pack(pady=30)
    bot3.pack(pady=10)

def inbetween():
    Tk.destroy(master)
    mainScreen()

mainScreen()
##