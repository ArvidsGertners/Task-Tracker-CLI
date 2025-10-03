import argparse
import json
import datetime
import os
from asyncio import tasks

parser = argparse.ArgumentParser(description="A Task Tracker CLI tool made in Python")

subParsers = parser.add_subparsers(dest="command")

addParser = subParsers.add_parser("add", help="Add a task")
addParser.add_argument("description", help="The task to add")

args = parser.parse_args()


def writeTask(jsonFile="tasks.json"):



    with open(jsonFile, "r+") as file:

        fileData = json.load(file)

        newTask = {
            "id": len(fileData["tasks"]) + 1,
            "description": args.description,
            "status": "todo",
            "createdAt": f"{datetime.datetime.now()}",
            "updatedAt": f"{datetime.datetime.now()}",
        }

        fileData["tasks"].append(newTask)

        file.seek(0)

        json.dump(fileData, file, indent=4)


if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump({"tasks": []}, file, indent=4)


if args.command == "add":
    writeTask()
