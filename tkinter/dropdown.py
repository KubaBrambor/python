from tkinter import *

root = Tk()
root.title("Dropdown Menu")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selected", command=show).pack()

root.mainloop()