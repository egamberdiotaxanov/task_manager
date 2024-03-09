import sqlite3

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
        print("Tasks:")
        for task in tasks:
            status = "Completed" if task[3] else "Not completed"
            print(f"{task[0]}. {task[1]} - Deadline: {task[2]} - Status: {status}")

def main():
    task_manager = TaskManager('tasks.db')

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            task = Task(description, deadline)
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.display_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    task_manager.conn.close()

if __name__ == "__main__":
    main()
