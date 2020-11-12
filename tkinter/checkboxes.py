from tkinter import *


root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()
    return myLabel

var = StringVar()

checkbutton = Checkbutton(root, text="Check that box", variable=var, onvalue="Switch On", offvalue="Switch Off")
checkbutton.deselect()
checkbutton.pack()

myButton = Button(root, text="Show current selection", command=show).pack()

root.mainloop()