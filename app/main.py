import task_manager
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def execute_command(commands: list[list[str]]) -> None:
    """
    Executes a command in the task manager.
    """
    manager = task_manager.TaskManager()
    
    for command in commands:
        if len(command) == 0:
            print("No command provided. Please try again.")
            continue

        if command[0] == "add":
            if len(command) != 2:
                print("Description is required to add a task.")
            else:
                description = command[1]
                id = manager.add_task(description)
                print(f"Task added with ID: {id}")

        elif command[0] == "delete":
            if len(command) != 2:
                print("Task ID is required to delete a task.")
            else:
                id = int(command[1])
                manager.delete_task(id)
                print(f"Task with ID {id} deleted.")

        elif command[0] == "list":
            if len(command) != 1:
                print("No additional parameters required")
            manager.view_tasks()

        elif command[0] == "progress":
            if len(command) != 2:
                print("Task ID is required to mark a task as in progress.")
            else:
                id = int(command[1])
                manager.mark_in_progress(id)
                print(f"Task with ID {id} marked as in progress.")

        elif command[0] == "complete":
            if len(command) != 2:
                print("Task ID is required to mark a task as completed.")
            else:
                id = int(command[1])
                manager.mark_completed(id)
                print(f"Task with ID {id} marked as completed.")

        elif command[0] == "update":
            if len(command) != 3:
                print("Task ID and new description are required to update a task.")
            else:
                id = int(command[1])
                description = command[2]
                manager.update_task(id, description)
                print(f"Task with ID {id} updated.")
        else:
            print("Unknown command. Skipping...")

def main():
    print("Welcome to the Task Manager!")
    commands = [
        ["add", "Boy groceries"],
        ["add", "Walk the dog"],
        ["list"],
        ["progress", "0"],
        ["complete", "1"],
        ["update", "0", "Programming"],
        ["delete", "1"],
        ["list"]
    ]
    execute_command(commands)

if __name__ == "__main__":
    main()
    