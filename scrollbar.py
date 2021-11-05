import tkinter as tk
import GUI1
import GUI2

# the first gui owns the root window
win1 = tk.Tk()
gui1 = GUI1.GUI(win1)
gui1.pack(fill="both", expand=True)

# the second GUI is in a Toplevel
win2 = tk.Toplevel(win1)
gui2 = GUI2.GUI(win2)
gui2.pack(fill="both", expand=True)

tk.mainloop() # main window that can be used to call other windows.