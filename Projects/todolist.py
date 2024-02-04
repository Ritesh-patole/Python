# Simple To-Do List

tasks = []

def display_tasks():
    print("\nTasks:")
    if not tasks:
        print("No tasks yet.")
    else:
        for task in tasks:
            print(f"- {task}")

def add_task(task):
    tasks.append(task)
    print(f"\nTask '{task}' added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"\nTask '{task}' removed successfully.")
    else:
        print("\nTask not found.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == "4":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
