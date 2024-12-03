#function to add to task
def add_task(tasks):
    task = input("Enter the Task; ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")
    
    #function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}.[{'x' if task['completed'] else ' '}] {task['tasks']}")
            
#function to mark task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
        tasks[task_index]['completed'] = True
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid input or index out of range!")
        
#function to remove A task
def remove_task(tasks):
    view_tasks(task_index)
            
    try:
        task_index = int(input ("Enter the index of the task to remove: ")) - 1
        del tasks[task_index]
        print("Task removed successfully!")
    except(IndexError, ValueError):
        print("Invalid input or index out of range!")
        
def main():
    tasks = []
    while True:
        print("\nTODO List Manager")
        print("1. Add a new Task")            
        print("2. View all Tasks")            
        print("3. Mark a Task as complete")
        print("4. Remove a task")     
        print("5. Exit")
        choice = input("Enter your choice: ")  
        
        if choice == "1":
            add_task(tasks)   
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting.... ")
            break
        else:
            print("Invalid choice! Please enter a number between 1 to 5.")
            
if __name__== "__main__":
                main()