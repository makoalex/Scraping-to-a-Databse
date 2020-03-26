import sqlite3
from clean_code import get_discount, get_price, get_cover, get_author, get_title, get_date, functions

connection = sqlite3.connect('Books.db')
c = connection.cursor()
for title, author, publish_date, cover, price, discount in functions:
    c.execute('INSERT INTO books VALUES (?,?,?,?,?,?)', functions)
connection.commit()
connection.close()