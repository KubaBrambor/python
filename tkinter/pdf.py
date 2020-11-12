from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("PDF opening")

def open():
    global my_img
    top = Toplevel()
    root.filename = filedialog.askopenfilename(initialdir="/calculator", title="Select A File", filetypes=(("png files", "*.png"),("jpg file", "*.jpg"),("all files", "*.*")))
    top.title(root.filename)
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lbl = Label(top, image=my_img).pack()
    
    

btn = Button(root, text="open", command=open).place(x=0, y=0)



mainloop()