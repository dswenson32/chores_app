import sqlite3, time
from flask import Flask, render_template, request

app = Flask(__name__)

# CREATE
# Future implementation

# READ
@app.route('/')
def index():
    conn = get_db_connection()
    chores = conn.execute('SELECT * FROM chores').fetchall()
    conn.close()
    print("we did it")
    return render_template('test.html', chores=chores)

# UPDATE
@app.route('/update')
def update():
    id = request.form.get("id")
    conn = get_db_connection()
    try:
        conn.execute('UPDATE chores SET last_performed=' + time.time() + 'WHERE id =' + id)
        conn.close()
        return "Success"
    except:
        conn.close()
        return "Failure"

# DELETE
# future implementation

# SUPPORT
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run()
