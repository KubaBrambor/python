"""
A program that stores book information:
Title, Author, Year, ISBN

User can:
- view all records
- search an entry
- add an entry
- update entry
- delete entry
- close
"""

from tkinter import *
from difflib import get_close_matches, SequenceMatcher
from backend import Database

class Frontend:

    def __init__(self):
        self.database = Database("lite.db")

    def get_selected_row(self,event):
        title.delete(0, END)
        author.delete(0, END)
        year.delete(0, END)
        isbn.delete(0, END)
        global currentItem
        list_size = listbox.size()
        if list_size != 0:
            index = listbox.curselection()
            currentItem = listbox.get(index)
            title.insert(0, currentItem[1])
            author.insert(0, currentItem[2])
            year.insert(0, currentItem[3])
            isbn.insert(0, currentItem[4])


    def view_command(self):
        listbox.delete(0, END)
        for row in self.database.view():
            listbox.insert(END, row)

    def search_command(self):
        listbox.delete(0, END)
        author = get_close_matches(author_text.get(), self.database.view_authors(), n=10, cutoff=0.3)
        title = get_close_matches(title_text.get(), self.database.view_titles(), n=10, cutoff=0.2)
        isbn = get_close_matches(isbn_text.get(), self.database.view_isbn(), n=10, cutoff=0.2)
        #combinations of queries
        #get author's book from specific year
        if author != [] and year_text.get() != "":
            for row in self.database.search(title_text.get(), author[0], year_text.get(), isbn_text.get()):
                listbox.insert(END, row)
        elif title != []:
            for row in self.database.search(title[0], "", "", ""):
                listbox.insert(END, row)
        elif author != []:
            for row in self.database.search("", author[0], "", ""):
                listbox.insert(END, row)
        elif isbn != []:
            for row in self.database.search("", "", "", isbn[0]):
                listbox.insert(END, row)
        elif year_text.get() != "":
            for row in self.database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
                listbox.insert(END, row)

    def add_command(self):
        self.database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        #show added book
        self.search_command()
        title.delete(0, END)
        author.delete(0, END)
        year.delete(0, END)
        isbn.delete(0, END)

    def delete_command(self):
        self.database.delete(currentItem[0])
        self.view_command()

    def update_command(self):
        self.database.update(currentItem[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        self.view_command()

frontend = Frontend()

root = Tk()
root.title("Books app")
root.geometry("580x380")

#frame for listbox and scrollbar
frame = LabelFrame(root, borderwidth=0, highlightthickness=0, height=70)

#buttons
viewAll = Button(frame, text="Pokaż wszystko", padx=30, pady=10, command = frontend.view_command)
search = Button(frame, text="Wyszukaj", padx=30, pady=10, command = frontend.search_command)
add = Button(frame, text="Dodaj", padx=30, pady=10, command = frontend.add_command)
update = Button(frame, text="Zmień", padx=30, pady=10, command = frontend.update_command)
delete = Button(frame, text="Usuń", padx=30, pady=10, command = frontend.delete_command)
close = Button(frame, text="Zamknij", padx=30, pady=10, command = root.destroy)

#scrollbar
scrollbar = Scrollbar(frame, activebackground='blue')

#listbox
listbox = Listbox(frame, height=15, width=40, yscrollcommand=scrollbar.set, exportselection=False)
scrollbar.config(command=listbox.yview)
listbox.bind('<<ListboxSelect>>', frontend.get_selected_row)
#inputs
title_text = StringVar()
title = Entry(root, textvariable=title_text, width=28, bd='1px', )
year_text = StringVar()
year = Entry(root, textvariable=year_text, width=28)
author_text = StringVar()
author = Entry(root, textvariable=author_text, width=28)
isbn_text = StringVar()
isbn = Entry(root, textvariable=isbn_text, width=28)

#labels
titleLabel = Label(root, text="Tytuł")
yearLabel = Label(root, text="Rok")
authorLabel = Label(root, text="Autor")
isbnLabel = Label(root, text="ISBN")

#title entry with label
titleLabel.grid(row=0, column=0, padx=(10,0), pady=(10,0))
title.grid(row=0, column=1, pady=(10,0))
#year entry with label
yearLabel.grid(row=1, column=0, padx=(10,0))
year.grid(row=1, column=1)
#author entry with label
authorLabel.grid(row=0, column=2, padx=(20,2), pady=(10,0))
author.grid(row=0, column=3, pady=(10,0))
#isbn entry with label
isbnLabel.grid(row=1, column=2, padx=(20,2))
isbn.grid(row=1, column=3)
#frame placed
frame.grid(row=2, column=0, columnspan=4, rowspan=6, pady=(20,0), padx=(0,0))
#listbox placed
listbox.grid(row=0, column=0, columnspan=2, rowspan=6, sticky='nsew', padx=(10,0))
#scrollbar placed
scrollbar.grid(row=0, column=2, rowspan=6, sticky='nsew')
#placing buttons
viewAll.grid(row=0, column=3, sticky="nsew", padx=(30, 0))
search.grid(row=1, column=3, sticky="nsew", padx=(30,0))
add.grid(row=2, column=3, sticky="nsew", padx=(30,0))
update.grid(row=3, column=3, sticky="nsew", padx=(30,0))
delete.grid(row=4, column=3, sticky="nsew", padx=(30,0))
close.grid(row=5, column=3, sticky="nsew", padx=(30,0))



root.mainloop()