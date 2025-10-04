A simple and efficient command-line task tracker built with Python. Manage your tasks with ease using intuitive commands to add, update, delete, and track task progress.

## Features

- ✅ Add new tasks
- ✏️ Update task descriptions
- 🗑️ Delete tasks
- 📋 List tasks (all or filtered by status)
- 🔄 Change task status (todo, in-progress, done)
- 💾 Persistent storage using JSON
- 🎯 Simple and intuitive CLI interface

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone or download the `task_tracker.py` file
2. Make sure you have Python installed on your system
3. No additional dependencies required (uses only Python standard library)

## Usage

### Basic Commands

**Add a new task:**
```bash
python task_tracker.py add "Complete project documentation"
```

**List all tasks:**
```bash
python task_tracker.py list
```

**List tasks by status:**
```bash
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done
```

**Update a task description:**
```bash
python task_tracker.py update 1 "Updated task description"
```

**Delete a task:**
```bash
python task_tracker.py delete 1
```

**Change task status:**
```bash
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1
python task_tracker.py mark-todo 1
```

### Help

Get help for any command:
```bash
python task_tracker.py --help
python task_tracker.py add --help
python task_tracker.py list --help
```

## Examples

```bash
# Add some tasks
python task_tracker.py add "Learn Python"
python task_tracker.py add "Build a CLI app"
python task_tracker.py add "Write documentation"

# List all tasks
python task_tracker.py list
# Output:
# ID: 1 - Learn Python
# ID: 2 - Build a CLI app
# ID: 3 - Write documentation

# Mark a task as in progress
python task_tracker.py mark-in-progress 1

# Mark a task as done
python task_tracker.py mark-done 2

# List only completed tasks
python task_tracker.py list done
# Output:
# ID: 2 - Build a CLI app

# Update a task description
python task_tracker.py update 3 "Write comprehensive documentation"

# Delete a task
python task_tracker.py delete 1
```

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is automatically created when you add your first task.

### Task Structure
Each task contains:
- `id`: Unique identifier
- `description`: Task description
- `status`: Current status (todo, in-progress, done)
- `createdAt`: Creation timestamp
- `updatedAt`: Last modification timestamp

Example `tasks.json`:
```json
{
    "tasks": [
        {
            "id": 1,
            "description": "Learn Python",
            "status": "done",
            "createdAt": "2025-10-04T17:28:16",
            "updatedAt": "2025-10-04T17:30:45"
        }
    ]
}
```

## Commands Reference

| Command | Description | Usage |
|---------|-------------|-------|
| `add` | Add a new task | `add "task description"` |
| `list` | List tasks | `list [todo\|in-progress\|done]` |
| `update` | Update task description | `update <id> "new description"` |
| `delete` | Delete a task | `delete <id>` |
| `mark-todo` | Mark task as todo | `mark-todo <id>` |
| `mark-in-progress` | Mark task as in progress | `mark-in-progress <id>` |
| `mark-done` | Mark task as done | `mark-done <id>` |

## File Structure

```
.
├── task_tracker.py    # Main application file
└── tasks.json         # Task data (created automatically)
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [ArvidsGertners](https://github.com/ArvidsGertners)

---

*Simple task management from the command line* 