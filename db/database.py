import sqlite3

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """ """


db.close()