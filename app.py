import sqlite3, time, json
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
@app.route('/update', methods = ["POST"])
def update():
    jsonObj = request.get_json()
    conn = get_db_connection()
    try:
        query = "UPDATE chores SET last_performed=" + str(round(time.time() * 1000)) + " WHERE id = " + jsonObj.get('id')
        print(query)
        conn.execute(query)
        conn.commit()
        conn.close()
        return "Success"
    except:
        conn.close()
        return "Failure", 500

# DELETE
# future implementation

# SUPPORT
def get_db_connection():
    conn = sqlite3.connect('/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run()
