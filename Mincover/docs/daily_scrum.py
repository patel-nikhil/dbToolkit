import sqlite3
import pprint
import csv

connection = sqlite3.connect('daily_scrum.db')
cursor = connection.cursor()

def create_table():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS Meeting (date TEXT, minutes TEXT)''')
    connection.commit()

def insert(notes):
    global cursor
    global connection
    cursor.execute("INSERT INTO Meeting VALUES (DATETIME('now', 'localtime'), ?)",
                   (notes,))
    connection.commit()

def view():
    global cursor
    print("date, minutes")
    cursor.execute("SELECT * FROM Meeting ORDER BY date")
    pprint.pprint(cursor.fetchall())

def export():
    global cursor
    global connection

    with open("daily_scrum.csv", "w") as f:
        f.write("Meeting(date, minutes)" + "\n")
        csvWriter = csv.writer(f)    
        cursor.execute("SELECT * FROM Meeting ORDER BY date")
        rows = cursor.fetchall()
        csvWriter.writerows(rows)


if __name__ == '__main__':
    create_table()
