import time
from datetime import datetime
current_time = datetime.now()
print("Current Date and Time:", current_time)

def all_task(task):
    if not task:
        print("\nYour to-do list is empty!")
    else:
        priority_order = {"high": 1, "medium": 2, "low": 3}
        task.sort(key=lambda x: priority_order.get(x["priority"].lower(), 3))

        print("\nYour To-Do List:")
        for index, task in enumerate(task):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['name']} - {task['Deadline']} - {task['priority']} - [{status}]")

def view_task(task):
    if not task:
        print("\nYour to-do list is empty!")
    else:
        # Define the priority order
        priority_order = {"high": 1, "medium": 2, "low": 3}

        # Sort tasks by priority
        task.sort(key=lambda x: priority_order.get(x["priority"].lower(), 3))
        
        # Display the sorted task list
        print("\nYour To-Do List:")
        for index, task in enumerate(task):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['name']} - {task['Deadline']} - {task['priority']} - [{status}]")
            
def add_task(task):
    task_name = input ("Name of the task that you want to add - ")
    date=(input("Set Deadline in [YYYY-MM-DD] for the task - "))
    priority = input("Input priority as HIGH, MEDIUM, LOW. Your Priority - ").lower()  # Convert to lowercase
    reminder_time = input("Set a reminder (HH:MM) or leave blank - ")
    task.append({"name":task_name , "completed":False ,"Deadline":date ,"priority":priority ,"reminder":reminder_time})
    print(f"{task_name} has been added to the TO-DO LIST")

def remove_task(task):
    if not task:
        print("Your list is Empty")
    else:
        all_task(task)
        task_number=int(input("\nNumber of the task that you want to remove :- "))
        if  task_number <= len(task):
            removed_task= task.pop(task_number)
            print(f"'{removed_task["name"]}' has been removed from your TO-DO LIST")
        else :
            print("Invalid task number.")

def task_completed(task):
    all_task(task)
    task_number = int(input("\nEnter the task number to mark as completed: ")) 
    if 0 <= task_number < len(task):
        task[task_number]["completed"] = True
        print(f"'{task[task_number]['name']}' has been marked as completed.")
    else:
        print("Invalid task number.")

def check_reminders(task):
    current_time = datetime.now().strftime("%H:%M")
    for t in task:
        if t["reminder"] and t["reminder"] == current_time and not t["completed"]:
            print(f"Reminder: You have a task '{t['name']}' due soon!")
    time.sleep(10)


def display_menu ():
    print ("\n--- TO DO LIST ---")
    print ("\n1. View Tasks")
    print ("2. Add Task")
    print ("3. Remove Task")
    print ("4. Mark task as Completed")
    print ("5. Exit")

def main() :

    task = []
    while True:
        display_menu()
        try:
            choice = int(input("\nSelect the option you want to execute: "))
            if choice == 1:
                view_task(task)
            elif choice == 2:
                add_task(task)
            elif choice == 3:
                remove_task(task)
            elif choice == 4:
                task_completed(task)
            elif choice == 5:
                print("Have you completed your task? - REMEMBER WHAT YOU WANT TO ACCOMPLISH")
                break
            else:
                print("\nInvalid option selected")
        except ValueError:
            print("Please select a valid option.")
        
if __name__ == "__main__":
    main()   