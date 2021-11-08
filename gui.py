from tkinter import *
DEBUG = False

window = Tk()
if DEBUG:
    window.attributes("-fullscreen", True)
window.geometry("800x480")

left_frame = Frame(window, width=266, height=480, bg='cyan')
left_frame.pack(side=LEFT)

right_frame = Frame(window, width=266, height=480, bg="red")
right_frame.pack(side=RIGHT)

middle_frame = Frame(window, width=266, height=480, bg="yellow")
middle_frame.pack()

left_btn = Button(left_frame, text="Curtains")
left_btn.pack(padx=106, pady=229)

right_btn = Button(right_frame, text="Lights")
right_btn.pack(padx=106, pady=229)

middle_btn = Button(middle_frame, text="Plant")
middle_btn.pack(padx=115, pady=229)

window.mainloop()


