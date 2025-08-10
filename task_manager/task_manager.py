from enum import Enum
import logging

logger = logging.getLogger(__name__)

class TaskStatus(Enum):
    """
    `TaskStatus` defines the possible statuses of a task.
    """

    PENDING = "Pending"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"


class Task:
    """
    `Task` represents a single task with three statuses:
    - `pending`: Task is created but not yet started.
    - `in_progress`: Task is currently being worked on.
    - `completed`: Task has been finished.
    """

    def __init__(self, description: str, status: TaskStatus = TaskStatus.PENDING):
        self._description = description
        self._status = status

    def mark_in_progress(self):
        """
        Marks the task as in progress.
        """
        self._status = TaskStatus.IN_PROGRESS

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self._status = TaskStatus.COMPLETED

    def mark_pending(self):
        """
        Marks the task as pending.
        """
        self._status = TaskStatus.PENDING

    def get_status(self):
        """
        Get task status
        """
        return self._status
    
    def get_description(self):
        """
        Get task description
        """
        return self._description
    
    def __str__(self):
        return f"Task(description={self._description}, status={self._status.value})"


class TaskManager:
    """
    `TaskManager` provides a way to manage tasks
    """

    def __init__(self):
        self._next_id = -1
        self._tasks: dict[int, Task] = {}

    def add_task(self, description: str) -> int:
        """
        Adds a new task with the given description.
        """
        logger.debug(f"Adding new task with id {self._next_id + 1}.")
        self._tasks[self._next_id + 1] = Task(description)
        self._next_id += 1
        return self._next_id

    def update_task(self, id: int, description: str) -> None:
        """
        Updates the description of the specified task.
        """
        if id in self._tasks:
            logger.debug(f"Updating task with id {id}.")
            self._tasks[id] = Task(description, self._tasks[id].get_status())
        else:
            logger.debug(f"Task with id {id} does not exist.")

    def delete_task(self, id: int) -> None:
        """
        Deletes the specified task.
        """
        if id in self._tasks.keys():
            logger.debug(f"Deleting task with id {id}.")
            self._tasks.pop(id)
        else:
            logger.debug(f"Task with id {id} does not exist.")

    def view_tasks(self) -> None:
        """
        Returns a list of all tasks.
        """
        if not self._tasks:
            logger.debug("No tasks available.")
        else:
            for id, task in self._tasks.items():
                print(f"Id={id}, {task}")

    def mark_in_progress(self, id: int) -> None:
        """
        Marks the specified task as in progress.
        """
        if id in self._tasks:
            logger.debug(f"Marking task with id {id} as in progress.")
            self._tasks[id].mark_in_progress()
        else:
            logger.debug(f"Task with id {id} does not exist.")

    def mark_completed(self, id: int) -> None:
        """
        Marks the specified task as completed.
        """
        if id in self._tasks:
            logger.debug(f"Marking task with id {id} as completed.")
            self._tasks[id].mark_completed()
        else:
            logger.debug(f"Task with id {id} does not exist.")

    def all_tasks(self) -> dict[int, Task]:
        """
        Returns all tasks.
        """
        return self._tasks

    def is_existed(self, id: int) -> bool:
        """
        Checks if a task with the given ID exists.
        """
        return id in self._tasks.keys()
