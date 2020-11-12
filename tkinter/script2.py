from tkinter import *

root = Tk()
stateOfButton = [True]
def changeState():
    stateOfButton2 = [not c for c in stateOfButton]
    stateOfButton[0] = stateOfButton2[0]
    if stateOfButton[0]:
        myButton2.config(state="disabled")
    else:
        myButton2.config(state="normal")

def inputFunc():
    myLabel = Label(root, text=myInput1.get())
    myLabel.grid(row=3, column=0)
    myButton2.config(text=myInput1.get())

# Creating label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="the second Hello World")
# Creating button
myButton1 = Button(root, text="Click me", command=changeState, fg="black", highlightbackground="black",
activebackground="black", activeforeground="white")
myButton2 = Button(root, text="The button2", state=DISABLED, command=inputFunc)
# Creating input field
myInput1 = Entry(root, width=50)
# Showing it on screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myButton1.grid(row=1, column=2)
myButton2.grid(row=2, column=1)
myInput1.grid(row=0, column=2)

root.mainloop()

