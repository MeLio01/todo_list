from dataclasses import dataclass
from typing import Dict, Any
from .model import Task as TaskDB
from project.extensions import db

# The class `Task` is a dataclass that provides a higher-level interface for working with tasks
@dataclass
class Task:
    id: str
    content: str
    completed: bool

    # Class method that creates an instance of the `Task` class from a `TaskDB` object
    @classmethod
    def instance_creator(cls, task_db: TaskDB):
        return cls(
            id = task_db.id,
            content = task_db.content,
            completed = task_db.completed,
        )
    
    # Class method that adds a new task to the database
    @classmethod
    def add_task(cls, taskinfo: Dict[str, Any]):
        task_db = TaskDB(
            content=taskinfo["content"],
            completed=taskinfo["completed"]
        )
        task_db.create()
        if task_db:
            return cls.instance_creator(task_db)
        return None
    
    # Class method that updates an existing task in the database
    @classmethod
    def update_task(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            task_db = task_db.update(**taskinfo)
            return cls.instance_creator(task_db)
        return None
    
    # Class method that deletes a task from the database
    @classmethod
    def delete_task(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            task_db.delete(force_delete=True)
            return True
        return False

    # Class method that updates the completion status of a task in the database
    @classmethod
    def update_task_status(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            task_db.completed = not task_db.completed
            task_db.update()
            return cls.instance_creator(task_db)
        return None
    
    # Class method that returns the instance of task by the given id
    @classmethod
    def get_task_by_id(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            return cls.instance_creator(task_db)
        return None
    
    # Class method that returns the instance of all the tasks
    @classmethod
    def get_all_tasks(cls):
        tasks = TaskDB.get_all()
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None
    
    # Class method that returns the instance of all the completed tasks
    @classmethod
    def get_completed_tasks(cls):
        tasks = TaskDB.get_all({"completed": True})
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None