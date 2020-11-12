from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.geometry("400x400")

def refresh(variable):
    global my_lbl
    my_lbl['text'] = horizontal.get()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL, command=refresh)
horizontal.pack()

my_lbl = Label(root, text=horizontal.get())
my_lbl.pack()



my_btn = Button(root, text="Refresh", command=refresh)
my_btn.pack()

root.mainloop()