import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# CREATE
# READ
# UPDATE
# DELETE

# SUPPORT
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/test')
def index():
    conn = get_db_connection()
    chores = conn.execute('SELECT * FROM chores').fetchall()
    conn.close()
    print("we did it")
    return render_template('test.html', chores=chores)

if __name__ == '__main__':
    app.run()
