from tkinter import *
import sqlite3


root=Tk()
root.title("Databases")
root.geometry("400x400")

# Create database or connecto to one
conn = sqlite3.connect('adress_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE adresses (
    first_name text,
    last_name text,
    adress text,
    city text,
    state text,
    zipcode integer
)""")


# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()