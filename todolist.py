print("To-Do List Application operations:")
print("1. Display To-Do List")
print("2. Add a Task")
print("3. Mark a Task as Completed")
print("4. Remove a Task")
print("5. Quit")
tasks = []
def display_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")
    else:
        print("Your to-do list is empty.")
def add_task():
    tname = input("Enter the task name: ")
    tasks.append({'name': tname, 'completed': False})
    print(f"Task '{tname}' added successfully.")
def mark_as_completed():
    display_tasks()
    tnum = int(input("Enter the task number to mark as completed: "))
    if 1 <= tnum <= len(tasks):
        tasks[tnum - 1]['completed'] = True
        print(f"Task '{tasks[tnum - 1]['name']}' marked as completed.")
    else:
        print("Invalid task number.")
def remove_task():
    display_tasks()
    tnum = int(input("Enter the task number to remove: "))
    if 1 <= tnum <= len(tasks):
        removed_task = tasks.pop(tnum - 1)
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task number.")
        
while True:
    choice = input("Enter your choice in between 1 to 5: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_as_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exit")
        break
    else:
        print("Invalid choice\nPlease enter a number between 1 to 5.")
        
