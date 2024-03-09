import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import pandas as pd
from openpyxl import Workbook

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                description TEXT,
                completed BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute('''
            INSERT INTO tasks (description, completed)
            VALUES (?, ?)
        ''', (task.description, task.completed))
        self.conn.commit()

    def display_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        tasks = self.cursor.fetchall()
        return tasks

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        self.conn.commit()

def add_task():
    description = entry_description.get()
    task = Task(description)
    task_manager.add_task(task)
    messagebox.showinfo("Success", "Task added successfully!")
    display_tasks()

def display_tasks():
    tasks = task_manager.display_tasks()
    tasks_str = "Tasks:\n"
    for task in tasks:
        status = "Completed" if task[2] else "Not completed"
        tasks_str += f"{task[0]}. {task[1]} - Status: {status}\n"
    label_tasks.config(text=tasks_str)

def delete_task():
    task_id = entry_task_id.get()
    task_manager.delete_task(task_id)
    messagebox.showinfo("Success", "Task deleted successfully!")
    display_tasks()

def save_to_excel():
    tasks = task_manager.display_tasks()
    wb = Workbook()
    ws = wb.active
    ws.append(["Task ID", "Description", "Completed"])
    for task in tasks:
        ws.append(task)
    wb.save("tasks.xlsx")
    messagebox.showinfo("Success", "Tasks saved to Excel file successfully!")

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    label_clock.config(text=current_time)
    root.after(1000, update_clock)

task_manager = TaskManager('tasks.db')

root = tk.Tk()
root.title("Task Manager")

label_description = tk.Label(root, text="Description:")
label_description.grid(row=0, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=0, column=1)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=2)

button_display_tasks = tk.Button(root, text="Display Tasks", command=display_tasks)
button_display_tasks.grid(row=1, column=0, columnspan=3)

label_tasks = tk.Label(root, text="Tasks:")
label_tasks.grid(row=2, column=0, columnspan=3)

label_task_id = tk.Label(root, text="Enter Task ID to Delete:")
label_task_id.grid(row=3, column=0)
entry_task_id = tk.Entry(root)
entry_task_id.grid(row=3, column=1)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.grid(row=3, column=2)

button_save_to_excel = tk.Button(root, text="Save to Excel", command=save_to_excel)
button_save_to_excel.grid(row=4, column=0, columnspan=3)

label_clock = tk.Label(root, text="")
label_clock.grid(row=5, column=0, columnspan=3)

update_clock()

root.mainloop()
