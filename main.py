import argparse
import json
import datetime
import os

TASKS_PATH = 'tasks.json'

parser = argparse.ArgumentParser(description="A Task Tracker CLI tool made in Python")

subParsers = parser.add_subparsers(dest="command", required=True)

addParser = subParsers.add_parser("add", help="Add a task")
addParser.add_argument("description", help="The task to add")

updateParser = subParsers.add_parser("update", help="Update a task")
updateParser.add_argument("id", help="The task ID to update")
updateParser.add_argument("newDescription", help="the new description of the task")

deleteParser = subParsers.add_parser("delete", help="Delete a task")
deleteParser.add_argument("id", help="The task ID to delete")

listParser = subParsers.add_parser("list", help="List all tasks")
listParser.add_argument("type", help="The type of task to list", choices=['todo', 'in-progress', 'done'], nargs='?')

markInProgress = subParsers.add_parser("mark-in-progress", help="Mark a task in progress")
markInProgress.add_argument("id", help="The task ID to mark in progress")

markDone = subParsers.add_parser("mark-done", help="Mark a task in done")
markDone.add_argument("id", help="The task ID to mark in done")

markToDo = subParsers.add_parser("mark-todo", help="Mark a task to be done")
markToDo.add_argument("id", help="The task ID to mark todo")

args = parser.parse_args()


def load_data():
    try:
        with open(TASKS_PATH, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {"tasks": []}
    except FileNotFoundError:
        return {"tasks": []}


def save_data(data):
    with open(TASKS_PATH, 'w') as f:
        json.dump(data, f, indent=4)


def get_new_id(tasks):
    used = {t["id"] for t in tasks}
    i = 1
    while i in used:
        i += 1
    return i


def get_task_index(tasks, wanted_id):
    for t in range(len(tasks)):
        if tasks[t]["id"] == int(wanted_id):
            return t
    return None


def now():
    return datetime.datetime.now().isoformat(timespec='seconds')


def add():
    data = load_data()

    new_task = {
        "id": get_new_id(data["tasks"]),
        "description": args.description,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now(),
    }

    data["tasks"].append(new_task)
    data["tasks"].sort(key=lambda t: t["id"])
    save_data(data)
    print("Added new task")


def update():
    data = load_data()
    task_index = get_task_index(data["tasks"], args.id)
    if task_index is None:
        print(f"Task with ID {args.id} not found!")
        return

    data["tasks"][task_index]["description"] = args.newDescription
    save_data(data)
    print(f"Updated task {args.id}")


def delete():
    data = load_data()
    task_index = get_task_index(data["tasks"], args.id)
    if task_index is None:
        print(f"Task with ID {args.id} not found!")
        return

    data["tasks"].pop(task_index)
    save_data(data)
    print(f"Deleted task {args.id}")


def list_tasks():
    data = load_data()
    tasks = data["tasks"]
    for t in tasks:
        if args.type == 'todo' and t["status"] == 'todo':
            print(f"ID: {t["id"]} - {t['description']}")
        if args.type == 'in-progress' and t["status"] == 'in-progress':
            print(f"ID: {t["id"]} - {t['description']}")

        if args.type == 'done' and t["status"] == 'done':
            print(f"ID: {t["id"]} - {t['description']}")

        if args.type is None:
            print(f"ID: {t["id"]} - {t['description']}")


def mark_in_progress():
    data = load_data()
    task_index = get_task_index(data["tasks"], args.id)
    if task_index is None:
        print(f"Task with ID {args.id} not found!")
        return

    data["tasks"][task_index]["status"] = 'in-progress'
    save_data(data)


def mark_done():
    data = load_data()
    task_index = get_task_index(data["tasks"], args.id)
    if task_index is None:
        print(f"Task with ID {args.id} not found!")
        return
    data["tasks"][task_index]["status"] = 'done'
    save_data(data)


def mark_to_do():
    data = load_data()
    task_index = get_task_index(data["tasks"], args.id)
    if task_index is None:
        print(f"Task with ID {args.id} not found!")
        return
    data["tasks"][task_index]["status"] = 'todo'
    save_data(data)


if args.command == "add":
    add()
elif args.command == "update":
    update()
elif args.command == "delete":
    delete()
elif args.command == "list":
    list_tasks()
elif args.command == "mark-in-progress":
    mark_in_progress()
elif args.command == "mark-done":
    mark_done()
elif args.command == "mark-todo":
    mark_to_do()
