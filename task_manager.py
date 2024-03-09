class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not completed"
            print(f"{index}. {task.description} - Deadline: {task.deadline} - Status: {status}")

    def mark_task_as_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_as_completed()
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid task number.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            task = Task(description, deadline)
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.display_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_as_completed(task_number)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
