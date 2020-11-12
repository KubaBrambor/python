from tkinter import *

window = Tk()

def km_to_miles():
    print(e1_value.get())
    t3.delete("1.0", END)
    t3.insert(END, int(e1_value.get())*1000)
    t1.delete("1.0", END)
    t1.insert(END, int(e1_value.get())*2.20462)
    t2.delete("1.0", END)
    t2.insert(END, int(e1_value.get())*35.274)

b1 = Button(window, text="Run", command=km_to_miles)
b1.grid(row=0, column=3)

l1 = Label(window, text="KG")
l1.grid(row=0, column=1)

l2 = Label(window, text="grams")
l2.grid(row=2, column=1)

l3 = Label(window, text="pounds")
l3.grid(row=2, column=2)

l4 = Label(window, text="ounces")
l4.grid(row=2, column=3)


e1_value=StringVar()
e1 = Entry(window, background='yellow', textvariable=e1_value)
e1.grid(row=0, column=2)

t1 = Text(window, height=1, width=30)
t1.grid(row=1, column=2)

t2 = Text(window, height=1, width=30)
t2.grid(row=1, column=3)

t3 = Text(window, height=1, width=30)
t3.grid(row=1, column=1)
window.mainloop()

