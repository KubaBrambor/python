from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Messagebox learning')

def popup():
    message = messagebox.askyesnocancel("This is my popoup", "hello world")
    
    if message == 1:
        Label(root, text="You clicked YES").pack()
    elif message == 0:
        Label(root, text="You clicked NO").pack()
    elif message == None:
        Label(root, text="You clicked CANCEL").pack()

Button(root, text="popup", command=popup).pack()


mainloop()