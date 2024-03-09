import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
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
                deadline TEXT,
                completed BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute('''
            INSERT INTO tasks (description, deadline, completed)
            VALUES (?, ?, ?)
        ''', (task.description, task.deadline, task.completed))
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
    deadline_str = entry_deadline.get()
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
    task = Task(description, deadline)
    task_manager.add_task(task)
    messagebox.showinfo("Success", "Task added successfully!")
    display_tasks()

def display_tasks():
    tasks = task_manager.display_tasks()
    tasks_str = "Tasks:\n"
    for task in tasks:
        status = "Completed" if task[3] else "Not completed"
        tasks_str += f"{task[0]}. {task[1]} - Deadline: {task[2]} - Status: {status}\n"
    label_tasks.config(text=tasks_str)

def delete_task():
    task_id = entry_task_id.get()
    task_manager.delete_task(task_id)
    messagebox.showinfo("Success", "Task deleted successfully!")
    display_tasks()

task_manager = TaskManager('tasks.db')

root = tk.Tk()
root.title("Task Manager")

label_description = tk.Label(root, text="Description:")
label_description.grid(row=0, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=0, column=1)

label_deadline = tk.Label(root, text="Deadline (YYYY-MM-DD HH:MM):")
label_deadline.grid(row=1, column=0)
entry_deadline = tk.Entry(root)
entry_deadline.grid(row=1, column=1)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=2, column=0, columnspan=2)

button_display_tasks = tk.Button(root, text="Display Tasks", command=display_tasks)
button_display_tasks.grid(row=3, column=0, columnspan=2)

label_tasks = tk.Label(root, text="Tasks:")
label_tasks.grid(row=4, column=0, columnspan=2)

label_task_id = tk.Label(root, text="Enter Task ID to Delete:")
label_task_id.grid(row=5, column=0)
entry_task_id = tk.Entry(root)
entry_task_id.grid(row=5, column=1)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.grid(row=6, column=0, columnspan=2)

root.mainloop()
