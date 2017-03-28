import sqlite3
import pprint
import csv

connection = sqlite3.connect('mincover.db')
cursor = connection.cursor()

# Product Backlog
# ProductBacklog(pid, story, estimation, priority)

def create_product_backlog():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS ProductBacklog (pid INTEGER, story TEXT,
              estimation INTEGER, priority INTEGER, PRIMARY KEY(pid))''')
    connection.commit()    


def view_product_backlog():
    global cursor
    global connection
    print("pid, story, est, priority")
    cursor.execute("SELECT * FROM ProductBacklog ORDER BY priority")
    print(cursor.fetchall())

def add_story(ID, story, estimation, priority):
    global cursor
    global connection
    cursor.execute("INSERT INTO ProductBacklog VALUES (?, ?, ?, ?)",
                   (ID, story, estimation, priority))
    connection.commit()


# Task
# Tasks(pid, taskID, desc)

def create_task_table():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (pid INTEGER, taskID INTEGER,
                    desc TEXT, PRIMARY KEY(pid, taskID),
                    FOREIGN KEY(pid) REFERENCES ProductBacklog(pid))''')
    connection.commit()


def view_tasks():
    global cursor
    global connection
    print("pid, taskID, description")
    cursor.execute("SELECT * FROM Tasks ORDER BY pid")
    pprint.pprint(cursor.fetchall())

def add_task(pid, taskID, description):
    global cursor
    global connection
    cursor.execute("INSERT INTO Tasks VALUES (?, ?, ?)",
                   (pid, taskID, description))
    connection.commit()



# Task Statuses
# TaskLog(taskID, date, weightLeft)

def create_task_log():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS TaskLog (pid INTEGER, taskID INTEGER, date TEXT NOT NULL,
              weightLeft INTEGER, PRIMARY KEY(pid, taskID, date),
              FOREIGN KEY (pid, taskID) REFERENCES Tasks(pid, taskID))''')
    connection.commit()


def view_task_log():
    global cursor
    global connection
    print("pid, taskID, time, weightRemaining")
    cursor.execute("SELECT * FROM TaskLog ORDER BY taskID")
    pprint.pprint(cursor.fetchall())

def update_sprint_task(pid, taskID, weight):
    global cursor
    global connection
    cursor.execute("INSERT INTO TaskLog VALUES (?, ?, DATETIME('now', 'localtime'), ?)",
                   (pid, taskID, weight))
    connection.commit()



# Sprint Log
# Sprint(num, start, end)

def create_sprint_log():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS Sprint (num INTEGER PRIMARY KEY, start TEXT,
              end TEXT)''')
    connection.commit()    

def view_sprint_log():
    global cursor
    global connection
    print("sprintNum, startTime, endTime")
    cursor.execute("SELECT * FROM Sprint ORDER BY num")
    pprint.pprint(cursor.fetchall())

def add_sprint(num):
    global cursor
    global connection
    cursor.execute("INSERT INTO Sprint VALUES (?, DATETIME('now', 'localtime'), ?)",
                   (num, None))
    connection.commit()


# Sprint Backlog
# SprintLog(num, pid, tid)

def create_sprint_backlog():
    global cursor
    global connection
    cursor.execute('''CREATE TABLE IF NOT EXISTS SprintLog (num INTEGER, pid INTEGER,
              tid INTEGER,
              FOREIGN KEY (num) REFERENCES Sprint(num),
              FOREIGN KEY(pid, tid) REFERENCES Tasks(pid, taskID))''')
    connection.commit()    


def view_sprint_backlog():
    global cursor
    global connection
    print("sprintNum, pid, taskID")
    cursor.execute("SELECT * FROM SprintLog ORDER BY num")
    pprint.pprint(cursor.fetchall())

def add_sprint_task(num, pid, tid):
    global cursor
    global connection
    cursor.execute("INSERT INTO SprintLog VALUES (?, ?, ?)",
                   (num, pid, tid))
    connection.commit()

def export():
    global cursor
    global connection

    with open("backlog.csv", "w") as f:
        f.write("ProductBacklog(pid, story, est, priority)" + "\n")
        csvWriter = csv.writer(f)    
##        cursor.execute("pragma table_info('ProductBacklog')")
##        write(csvWriter, cursor)
        cursor.execute("SELECT * FROM ProductBacklog ORDER BY priority")
        write(csvWriter, cursor)

    with open("tasks.csv", "w") as f:
        f.write("Tasks(pid, taskID, description)" + "\n")
        csvWriter = csv.writer(f) 
##        cursor.execute("pragma table_info('Tasks')")
##        write(csvWriter, cursor)
        cursor.execute("SELECT * FROM Tasks ORDER BY taskID")
        write(csvWriter, cursor)

    with open("tasklog.csv", "w") as f:
        f.write("Tasklog(pid, taskID, time, weightRemaining)" + "\n")
        csvWriter = csv.writer(f)
##        cursor.execute("pragma table_info('Tasklog')")
##        write(csvWriter, cursor)
        cursor.execute("SELECT * FROM TaskLog ORDER BY taskID")
        write(csvWriter, cursor)

    with open("sprints.csv", "w") as f:
        f.write("Sprint(sprintNum, startTime, endTime)" + "\n")
        csvWriter = csv.writer(f)
##        cursor.execute("pragma table_info('Sprint')")
##        write(csvWriter, cursor)
        cursor.execute("SELECT * FROM Sprint ORDER BY num")
        write(csvWriter, cursor)

    with open("sprintlog.csv", "w") as f:
        f.write("SprintLog(sprintNum, pid, taskID)" + "\n")
        csvWriter = csv.writer(f)
##        cursor.execute("pragma table_info('Sprintlog')")
##        write(csvWriter, cursor)
        cursor.execute("SELECT * FROM SprintLog ORDER BY num")
        write(csvWriter, cursor)

def write(csvWriter, cursor):    
    rows = cursor.fetchall()
    csvWriter.writerows(rows)

if __name__ == '__main__':
    create_product_backlog()
    create_task_table()
    create_task_log()
    create_sprint_log()
    create_sprint_backlog()
