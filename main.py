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

args = parser.parse_args()


def load_data():
    if not os.path.exists(TASKS_PATH):
        return {"tasks": []}
    with open(TASKS_PATH, 'r') as f:
        return json.load(f)


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
    data["tasks"][get_task_index(data["tasks"], args.id)]["description"] = args.newDescription
    save_data(data)


if args.command == "add":
    add()
elif args.command == "update":
    update()
