from tkinter import *

root = Tk()
root.title("Frame lesson")


frame = LabelFrame(root, text="this is my frame", padx=90, pady=40)
frame.pack(padx=10, pady=10)

button = Button(frame, text='click me')
button2 = Button(frame, text='not click')
button.grid(row=0, column=0)
button2.grid(row=0, column=1)

root.mainloop()