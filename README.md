# Task Manager CLI

A lightweight command-line task manager built in Python — no dependencies required.

## Overview

A simple but feature-rich terminal tool for managing tasks with deadlines, status tracking, and filtering. Track what's in progress, overdue, or completed without leaving the terminal.

## Features

- Add tasks with optional deadlines (DD-MM-YYYY format)
- View all tasks with completion status and deadlines
- Mark tasks as done (with auto-recorded completion timestamp)
- Delete tasks by index
- Filter tasks by status: completed, outstanding, overdue, or not overdue
- Custom status labels (e.g. "blocked", "in review")

## Getting Started
```bash
git clone https://github.com/yourusername/task-manager-cli
cd task-manager-cli
python task_manager.py
```

No external dependencies — just the Python standard library.

## API Reference

| Function | Parameters | Description |
|----------|-----------|-------------|
| `add_task` | `tasks, description, deadline_str=None` | Adds a new task, optionally with a deadline |
| `view_tasks` | `tasks` | Prints all tasks with index, status, and deadline |
| `mark_task_done` | `tasks, task_index` | Marks a task complete and records the timestamp |
| `delete_task` | `tasks, task_index` | Removes a task by index |
| `filter_tasks` | `tasks, filter_type` | Filters tasks — see filter options below |
| `update_status` | `tasks, task_index, new_status` | Sets a custom status string on a task |

### Filter options

| Filter | Description |
|--------|-------------|
| `"completed"` | Tasks marked as done |
| `"outstanding"` | Tasks not yet completed |
| `"overdue"` | Incomplete tasks past their deadline |
| `"not overdue"` | Incomplete tasks with a future deadline |

## Task Structure

Each task is stored as a dictionary with the following fields:
```python
{
    "description": str,
    "completed": bool,
    "created_on": datetime,
    "completed_on": datetime | None,
    "deadline": date | None,
    "status": str           # default: "in progress"
}
```

## Example Usage
```python
tasks = []

add_task(tasks, "Buy groceries", "15-06-2025")
add_task(tasks, "Finish report")
view_tasks(tasks)

mark_task_done(tasks, 0)
filter_tasks(tasks, "outstanding")
update_status(tasks, 1, "blocked")
delete_task(tasks, 0)
```

## File Structure
```
task-manager-cli/
└── task_manager.py    # All functions — ready to import or run directly
```

## License

MIT
