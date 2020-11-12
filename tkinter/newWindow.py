from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("New windows in Tkinter")

def open():
    global my_img
    global top
    if top is not None:
        top.destroy()
    top = Toplevel()
    top.title("Second window")
    my_img = ImageTk.PhotoImage(Image.open("images/1.png"))
    my_lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close", command=top.destroy).pack()

btn = Button(root, text='open another window', command=open).pack()

top = None
mainloop()