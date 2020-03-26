import sqlite3
from clean_code import all_data
connection = sqlite3.connect('Books.db')
c = connection.cursor()
c.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)",all_data)
connection.commit()
connection.close()