from datetime import datetime, date

def add_task(tasks, task_description, deadline_str=None):
    deadline = None
    if deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY (e.g., 09-09-2025). Deadline not set.")
    
    new_task = {
        "description": task_description,
        "completed": False,
        "created_on": datetime.now(),
        "completed_on": None,
        "deadline": deadline,
        "status": "in progress"
    }
    tasks.append(new_task)
    print(f"Task '{task_description}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list")
        return

    print("\nYour Tasks")
    for i, task in enumerate(tasks):
        status = "[X]" if task["completed"] else "[ ]"
        deadline = f" (Deadline: {task['deadline']})" if task['deadline'] else ""
        print(f"{i + 1}. {status} {task['description']} | Status: {task['status']}{deadline}")
    print("======================")

def mark_task_done(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        tasks[task_index]["completed_on"] = datetime.now()
        tasks[task_index]["status"] = "completed"
        print(f"Task '{tasks[task_index]['description']}' marked as done.")
    else:
        print("Task Not Found")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['description']}' deleted.")
    else:
        print("Task Not Found")

def filter_tasks(tasks, filter_type):
    today = date.today()

    if filter_type == "completed":
        filtered = [t for t in tasks if t["completed"]]
    elif filter_type == "outstanding":
        filtered = [t for t in tasks if not t["completed"]]
    elif filter_type == "overdue":
        filtered = [t for t in tasks if t["deadline"] and t["deadline"] < today and not t["completed"]]
    elif filter_type == "not overdue":
        filtered = [t for t in tasks if t["deadline"] and t["deadline"] >= today and not t["completed"]]
    else:
        print("Invalid filter type.")
        return

    if not filtered:
        print(f"No tasks found for filter: {filter_type}")
    else:
        view_tasks(filtered)

def update_status(tasks, task_index, new_status):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["status"] = new_status
        print(f"Task '{tasks[task_index]['description']}' status updated to {new_status}.")
    else:
        print("Task Not Found")
