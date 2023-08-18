# Task Scheduler Python Project README

This Markdown README provides an overview and usage guide for the **Task Scheduler** Python project. The project aims to facilitate the management of Windows scheduled tasks using the `win32com.client` library. With this project, you can easily create, manage, toggle, run, and delete scheduled tasks programmatically.

## Installation

Before using the Task Scheduler Python project, make sure you have the required dependencies installed. You can install the necessary packages using the following command:

```bash
pip install pywin32
```

## Getting Started

To begin using the Task Scheduler, follow these steps:

1. Import the `win32com.client` module:

```python
import win32com.client
```

2. Create an instance of the `TaskScheduler` class:

```python
task_scheduler = TaskScheduler()
```

## Creating a Task

You can create a new scheduled task using the `create_task` method. Provide the task name, executable path, arguments, and trigger (in ISO 8601 format) as parameters.

```python
task_scheduler.create_task(
    task_name="MyTask",
    executable_path="C:\\path\\to\\executable.exe",
    arguments="--option value",
    trigger="2023-08-20T10:00:00"
)
```

## Getting All Tasks

Retrieve a list of all tasks with their details using the `get_all_tasks` method.

```python
all_tasks = task_scheduler.get_all_tasks()
for task in all_tasks:
    print(task)
```

## Toggling a Task

Toggle the enable/disable state of a task using the `toggle_task` method.

```python
# Enable the task
task_scheduler.toggle_task(task_name="MyTask", enable=True)

# Disable the task
task_scheduler.toggle_task(task_name="MyTask", enable=False)
```

## Running a Task

Run a specific task using the `run_task` method. The task will only run if it is enabled.

```python
task_scheduler.run_task(task_name="MyTask")
```

## Deleting a Task

Delete a scheduled task using the `delete_task` method.

```python
task_scheduler.delete_task(task_name="MyTask")
```

## Example

Here's an example that demonstrates the complete workflow:

```python
import win32com.client

# Create an instance of TaskScheduler
task_scheduler = TaskScheduler()

# Create a new task
task_scheduler.create_task(
    task_name="MyTask",
    executable_path="C:\\path\\to\\executable.exe",
    arguments="--option value",
    trigger="2023-08-20T10:00:00"
)

# Get all tasks
all_tasks = task_scheduler.get_all_tasks()
for task in all_tasks:
    print(task)

# Toggle task state
task_scheduler.toggle_task(task_name="MyTask", enable=True)

# Run the task
task_scheduler.run_task(task_name="MyTask")

# Delete the task
task_scheduler.delete_task(task_name="MyTask")
```

## Conclusion

The Task Scheduler Python project provides a convenient way to interact with the Windows Task Scheduler using Python and the `win32com.client` library. You can easily create, manage, toggle, run, and delete scheduled tasks, making task automation a breeze. Explore the methods provided by the `TaskScheduler` class to customize and enhance your task scheduling workflow.
