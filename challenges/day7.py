from operator import truediv
import os
from pickle import TRUE
from pickletools import uint8

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1) # split. from right side
                tasks.append({"text": text, "status" : status})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status= "done" if task["done"] else "not_done"
            f.write(f"{task["text"]}||{status}\n") 

def display_tasks(tasks):
    if not tasks:
        print(f"No tasks found!")
    else: 
        for i, task in enumerate(tasks,1):
            checkbox = "✅" if task['done'] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n------ Task manager--------")
        print("1. Add Task")
        print("2. View tasks")
        print("1. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text: 
                    tasks.append({"text": text, "done": False})
                    save_tasks(tasks)
                else: 
                    print("Task can't be empty")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try: 
                    num = int(input("Enter task number"))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = TRUE
                        save_tasks(tasks)
                        print("task marked as Done")
                    else: 
                        print("Invalid task number")
                except:
                    print("Please enter a number!")
            case "4":
                display_tasks(tasks)
                try: 
                    num = int(input("Enter task number which need to delete"))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else: 
                        print("Invalid task number")
                except:
                    print("Please enter a number!")
            case "5":
                print("Exiting task manager")
                break
            case _:
                print("Please choose a valid option!")

task_manager()