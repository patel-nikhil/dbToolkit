import sqlite3
import pprint
import csv

connection = sqlite3.connect('retrospection.db')
cursor = connection.cursor()

def create_table():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS Reflection (date TEXT, minutes TEXT)''')
    connection.commit()

def insert(notes):
    global cursor
    global connection
    cursor.execute("INSERT INTO Reflection VALUES (DATETIME('now', 'localtime'), ?)",
                   (notes,))
    connection.commit()

def view():
    global cursor
    print("date, retrospection")
    cursor.execute("SELECT * FROM Reflection ORDER BY date")
    pprint.pprint(cursor.fetchall())

def export():
    global cursor
    global connection

    with open("retrospection.csv", "w") as f:
        f.write("Reflection(date, minutes)" + "\n")
        csvWriter = csv.writer(f)    
        cursor.execute("SELECT * FROM Reflection ORDER BY date")
        rows = cursor.fetchall()
        csvWriter.writerows(rows)


if __name__ == '__main__':
    create_table()
