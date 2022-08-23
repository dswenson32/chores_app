import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('third', 'd', 1661223595)
            )
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ( 'second', 'd', 1651223595)
            )
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Furst', 'd', 1641223595)
            )







cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean that', 'w', 1641223595)
            )

connection.commit()
connection.close()