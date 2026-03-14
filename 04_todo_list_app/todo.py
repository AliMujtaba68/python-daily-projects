# todo.py

import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    else:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

# Main program
def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        print("Options: [A]dd, [D]elete, [Q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif choice == "d":
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx-1)
                    print(f"Removed: {removed}")
                    save_tasks(tasks)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()