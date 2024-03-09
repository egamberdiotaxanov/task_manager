import sqlite3
from openpyxl import Workbook

# Ma'lumotlar bazasi yaratish va bog'lanish
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Task jadvalini yaratish
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, description TEXT, completed BOOLEAN)''')


def add_task(description):
    c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, False))
    conn.commit()


def get_tasks():
    c.execute("SELECT * FROM tasks")
    return c.fetchall()


def mark_task_as_completed(task_id):
    c.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
    conn.commit()


def export_to_excel():
    wb = Workbook()
    ws = wb.active
    ws.append(['ID', 'Description', 'Completed'])

    tasks = get_tasks()
    for task in tasks:
        ws.append(task)

    wb.save("tasks.xlsx")


# Task qo'shish
add_task("Task 1")
add_task("Task 2")

# Tasklarni excel faylga saqlash
export_to_excel()

# DB bilan ishlashni yakunlash
conn.close()
