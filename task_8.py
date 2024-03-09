import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        tasks_str = "Tasks:\n"
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not completed"
            tasks_str += f"{i}. {task.description} - Status: {status}\n"
        return tasks_str

def add_task():
    description = entry_description.get()
    task = Task(description)
    task_manager.add_task(task)
    display_tasks()

def display_tasks():
    tasks_text.config(text=task_manager.display_tasks())

def choose_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((150, 150))  # Resize the image
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

task_manager = TaskManager()

root = tk.Tk()
root.title("Task Manager")

label_description = tk.Label(root, text="Description:")
label_description.grid(row=0, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=0, column=1)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=2)

tasks_text = tk.Label(root, text="")
tasks_text.grid(row=1, column=0, columnspan=3)

button_choose_image = tk.Button(root, text="Choose Image", command=choose_image)
button_choose_image.grid(row=2, column=0, columnspan=3)

image_label = tk.Label(root)
image_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
