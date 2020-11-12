import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='kurs' user='postgres' password='postgres' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='kurs' user='postgres' password='postgres' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

# insert("Water Glass", 10, 9.99)
# insert("Coconut Water", 20, 14.99)

def view():
    conn = psycopg2.connect("dbname='kurs' user='postgres' password='postgres' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='kurs' user='postgres' password='postgres' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s',(item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='kurs' user='postgres' password='postgres' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))
    conn.commit()
    conn.close()



print(view())
