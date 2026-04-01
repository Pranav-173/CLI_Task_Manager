import json

tasks = []

def s_input(x):
    try:
        return int(input(x))
    except:
        print("Invalid input.")
        return None

def show_tasks():
    print("\n--- TASK LIST ---")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "x" if task["done"] else " "
            print(f"{i + 1}. [{status}] {task['task']}")
    print("-----------------\n")

def add_task():
    task = input("Enter the task: ")
    if not task.strip():
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "done": False})
    print("Task Added !!")
    save_tasks()

def delete_task():
    show_tasks()
    index = s_input("Enter task number to delete: ")
    if index is None:
        return
    index -= 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task Deleted !!")
        save_tasks()
    else:
        print("Invalid index")

def mark_done():
    show_tasks()
    index = s_input("Enter task number to mark as done: ")
    if index is None:
        return
    index -= 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task marked as completed.")
        save_tasks()
    else:
        print("Invalid index")

def clear_tasks():
    global tasks
    confirm = input("Delete ALL tasks? (y/n): ")
    if confirm.lower() == "y":
        tasks = []
        save_tasks()
        print("All tasks deleted.")

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []
load_tasks()

while True:
    print("\n***** Available Operations *****")
    print("1. Show tasks\n2. Add Task\n3. Delete Task\n4. Mark task as done\n5. Clear Tasks\n6. Exit")
    print("*********************************")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1: show_tasks()
        elif choice == 2: add_task()
        elif choice == 3: delete_task()
        elif choice == 4: mark_done()
        elif choice == 5: clear_tasks()
        elif choice == 6: 
            print("Exiting....")
            break
    except:
        print("Invalid Choice.")
