import sqlite3

connection = sqlite3.connect('/app/database.db')

with open('/app/flaskapp/schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()