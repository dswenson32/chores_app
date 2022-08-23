import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Take out trash', 'd', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Load/unload dishwasher', 'd', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean off counter', 'd', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Run/fold laundry', 'd', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean cat litter', 'd', 1659352167000))







cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean bathrooms', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Sweep/mop floors', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Disinfect counter', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean stovetop', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean microwave', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean out fridge', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Dusting surfaces', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Replace hand towels', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean office', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Wash bedsheets', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Vacuum living room', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Vacuum bedroom', 'w', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Vacuum kid\'s room', 'w', 1659352167000))

cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean out cabinets', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Wash inside of fridge', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Reorganize cupboard', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Reorganize closets', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Vacuum couches', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean baseboards and corners', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Wash windows', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Dust fans and vents', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Clean car', 'm', 1659352167000))
cur.execute("INSERT INTO chores (chore_name, frequency, last_performed) VALUES (?, ?, ?)",
            ('Check AC Filter', 'm', 1659352167000))

connection.commit()
connection.close()