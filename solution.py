import json
import os

class TaskManager:
    def __init__(self):
        # File name where tasks will be stored
        self.file_name = "tasks.json"
        
        # Load existing tasks from file (if exists)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Check if file exists
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                try:
                    # Load tasks from JSON file
                    return json.load(file)
                except:
                    # Return empty list if file is empty/corrupted
                    return []
        return []

    def save_tasks(self):
        # Save tasks list into JSON file
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        # Take input from user
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        # Create a new task with completed = False
        task = {
            "title": title,
            "description": description,
            "completed": False
        }

        # Add task to list and save
        self.tasks.append(task)
        self.save_tasks()

        print("Task added successfully!\n")

    def view_tasks(self):
        # Check if task list is empty
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\nYour Tasks:")

        # Display all tasks with numbering
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['title']} - {task['description']} [{status}]")
        print()

    def delete_task(self):
        # Show current tasks before deleting
        self.view_tasks()

        if not self.tasks:
            return

        try:
            # Take task number from user
            num = int(input("Enter task number to delete: "))

            # Validate input range
            if 1 <= num <= len(self.tasks):
                deleted = self.tasks.pop(num - 1)
                self.save_tasks()
                print(f"Deleted: {deleted['title']}\n")
            else:
                print("Invalid number!\n")

        except:
            print("Invalid input!\n")

    def mark_completed(self):
        # Show tasks before marking
        self.view_tasks()

        if not self.tasks:
            return

        try:
            # Take task number input
            num = int(input("Enter task number to mark as completed: "))

            # Validate range
            if 1 <= num <= len(self.tasks):
                # Mark the task as completed
                self.tasks[num - 1]["completed"] = True
                self.save_tasks()
                print("Task marked as completed!\n")
            else:
                print("Invalid number!\n")

        except:
            print("Invalid input!\n")


def main():
    # Create TaskManager object
    manager = TaskManager()

    # Loop to keep program running
    while True:
        print("===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        # Take user choice
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.delete_task()
        elif choice == "4":
            manager.mark_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


# Run the program
if __name__ == "__main__":
    main()