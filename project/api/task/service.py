from typing import Dict, Any
from flask import jsonify
from .interface import Task

def delete_task_service(taskinfo: Dict[str, Any]):
    response = Task.delete_task(taskinfo)
    if response == True:
        return jsonify("Task Deleted!")
    else:
        return None