import sqlite3
import itertools

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        #for compination - get books for author from specific year
        if (year != "") and (author != ""):
            self.cur.execute("SELECT * FROM books WHERE author=? AND year=?",(author, year))
            print("executed")
        else:
            self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
            print("else executed")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        self.conn.commit()

    def view_authors(self):
        self.cur.execute("SELECT DISTINCT author FROM books")
        authors_touples = self.cur.fetchall()
        authors_array = list(itertools.chain(*authors_touples))
        return authors_array

    def view_titles(self):
        self.cur.execute("SELECT DISTINCT title FROM books")
        titles_touples = self.cur.fetchall()
        titles_array = list(itertools.chain(*titles_touples))
        return titles_array

    def view_isbn(self):
        self.cur.execute("SELECT DISTINCT isbn FROM books")
        isbns_touples = self.cur.fetchall()
        isbns_array = list(itertools.chain(*isbns_touples))
        isbns_to_string = [str(isbn) for isbn in isbns_array]
        return isbns_to_string

    def __del__(self):
        self.conn.close()

