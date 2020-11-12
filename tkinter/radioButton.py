from tkinter import *

root = Tk()
root.title("Radio Buttons learning")

# r = IntVar()
# r.set("2")

pizza = StringVar()

def clicked(value):
    myLabel = Label(root, text=value).pack()

modes = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mashroom", "Mashroom"),
    ("Onion", "Onion")
]

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

Button(root, text="add", command=lambda: clicked(pizza.get())).pack()



root.mainloop()