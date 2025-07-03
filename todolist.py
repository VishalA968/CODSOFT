#  To-Do List Application

todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks in the list.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{i}. {task['task']} - [{status}]")
    print()

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added!\n")

def update_task():
    show_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[index]['task'] = new_task
            print("Task updated!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]['done'] = True
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Task '{removed['task']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("End Task! ")
            break
        else:
            print("Invalid choice. Please enter 1-6.\n")

if __name__ == "__main__":
    main()
