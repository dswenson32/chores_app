import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO chores (chore_name, frequency) VALUES (?, ?)",
            ('Clean this', 'd')
            )

cur.execute("INSERT INTO chores (chore_name, frequency) VALUES (?, ?)",
            ('Clean that', 'w')
            )

connection.commit()
connection.close()