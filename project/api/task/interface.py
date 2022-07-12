from dataclasses import dataclass
from typing import Dict, Any

from .model import Task as TaskDB

@dataclass
class Task:
    id: str
    content: str
    completed: bool
    date_created: str

    @classmethod
    def instance_creator(cls, task_db: TaskDB):
        return cls(
            id = task_db.id,
            content = task_db.content,
            completed = task_db.completed,
            date_created = task_db.date_created
        )
    
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
    
    @classmethod
    def update_task(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            task_db = task_db.update(**taskinfo)
            return cls.instance_creator(task_db)
        return None
    
    @classmethod
    def delete_task(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            task_db.delete()
            return True
        return False
    
    @classmethod
    def get_task_by_id(cls, taskinfo: Dict[str, Any]):
        task_db: TaskDB = TaskDB.get_first({"id": taskinfo["id"]})
        if task_db:
            return cls.instance_creator(task_db)
        return None
    
    @classmethod
    def get_all_tasks(cls):
        tasks = TaskDB.get_all()
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None
    
    @classmethod
    def get_tasks_by_completed(cls, taskinfo: Dict[str, Any]):
        tasks = TaskDB.get_all({"completed": taskinfo["completed"]})
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None
    
    @classmethod
    def get_tasks_by_content(cls, taskinfo: Dict[str, Any]):
        tasks = TaskDB.get_all({"content": taskinfo["content"]})
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None
    
    @classmethod
    def get_tasks_by_date_created(cls, taskinfo: Dict[str, Any]):
        tasks = TaskDB.get_all({"date_created": taskinfo["date_created"]})
        if tasks:
            return [cls.instance_creator(task) for task in tasks]
        return None