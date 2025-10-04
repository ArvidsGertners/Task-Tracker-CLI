import argparse
import json
import datetime

TASKS_PATH = 'tasks.json'


def setup_parsers():
    parser = argparse.ArgumentParser(description="A Task Tracker CLI tool made in Python")
    sub_parsers = parser.add_subparsers(dest="command", required=True)

    # Add parser
    add_parsers = sub_parsers.add_parser("add", help="Add a task")
    add_parsers.add_argument("description", help="The task to add")

    # Update parser
    update_parser = sub_parsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", help="The task ID to update", type=int)
    update_parser.add_argument("newDescription", help="the new description of the task")

    # List parser
    list_parser = sub_parsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("type", help="The type of task to list",
                            choices=['todo', 'in-progress', 'done'], nargs='?')

    # Helper function for ID-based commands
    def create_task_id_parser(name, help_text):
        p = sub_parsers.add_parser(name, help=help_text)
        p.add_argument("id", help="The task ID", type=int)
        return p

    create_task_id_parser("delete", "Delete a task")
    create_task_id_parser("mark-in-progress", "Mark a task in progress")
    create_task_id_parser("mark-done", "Mark a task as done")
    create_task_id_parser("mark-todo", "Mark a task as todo")

    return parser.parse_args()


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


def get_task(task_id):
    data = load_data()
    task_index = get_task_index(data["tasks"], task_id)
    if task_index is None:
        print(f"Task with ID {task_id} not found!")
        return None, None
    return data, task_index


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
    data, index = get_task(args.id)

    if data is None:
        return

    data["tasks"][index]["description"] = args.newDescription
    data["tasks"][index]["updatedAt"] = now()
    save_data(data)
    print(f"Updated task {args.id}")


def delete():
    data, index = get_task(args.id)

    if data is None:
        return

    data["tasks"].pop(index)
    save_data(data)
    print(f"Deleted task {args.id}")


def list_tasks():
    data = load_data()
    tasks = data["tasks"]

    for t in tasks:
        # Show task if no filter specified OR status matches filter
        if args.type is None or t["status"] == args.type:
            print(f'ID: {t["id"]} - {t["description"]}')


def update_status(task_id, new_status):
    data, index = get_task(args.id)
    if data is None:
        return

    data["tasks"][index]["status"] = new_status
    data["tasks"][index]["updatedAt"] = now()
    save_data(data)
    print(f"Task {task_id} marked as {new_status}")


def mark_in_progress():
    update_status(args.id, 'in-progress')


def mark_done():
    update_status(args.id, 'done')


def mark_to_do():
    update_status(args.id, 'todo')


COMMANDS = {
    "add": add,
    "update": update,
    "delete": delete,
    "list": list_tasks,
    "mark-in-progress": mark_in_progress,
    "mark-done": mark_done,
    "mark-todo": mark_to_do,
}

if __name__ == "__main__":
    args = setup_parsers()
    if args.command in COMMANDS:
        COMMANDS[args.command]()
