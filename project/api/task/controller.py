import os
from flask import Blueprint, request

from .interface import Task
from .schema import task_schema, task_out_schema, task_id_schema, task_date_schema

from project.lib.errors import BadRequest

task_blueprint = Blueprint("task", __name__)

def create_task():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = task_schema.load(request.json)
    task = Task.add_task(data)
    response = task_out_schema.dump(task)
    return response, 200

def get_task_by_id():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = task_id_schema.load(request.json)
    task = Task.get_task_by_id(data)
    if task == None:
        raise BadRequest("Task not found", 400)
    response = task_out_schema.dump(task)
    return response, 200

def update_task():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = task_id_schema.load(request.json)
    task = Task.update_task(data)
    if task == None:
        raise BadRequest("Task not found", 400)
    response = task_out_schema.dump(task)
    return response, 200

def delete_task():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = task_id_schema.load(request.json)
    response = Task.delete_task(data)
    if response == False:
        raise BadRequest("Task not found", 400)
    return response, 200

def get_all_tasks():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    tasks = Task.get_all_tasks()
    if tasks == None:
        raise BadRequest("Task not found", 400)
    return {"tasks": tasks}, 200

def get_tasks_by_date_created():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = task_date_schema.load(request.json)
    tasks = Task.get_tasks_by_date_created(data)
    if tasks == None:
        raise BadRequest("Task not found", 400)
    return {"tasks": tasks}, 200

def get_completed_tasks():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    tasks = Task.get_completed_tasks(request.json)
    if tasks == None:
        raise BadRequest("Task not found", 400)
    return {"tasks": tasks}, 200

task_blueprint.add_url_rule("task/create", view_func=create_task, methods=["POST"])
task_blueprint.add_url_rule("task/get_task_by_id", view_func=get_task_by_id, methods=["GET"])
task_blueprint.add_url_rule("task/update", view_func=update_task, methods=["POST", "PUT"])
task_blueprint.add_url_rule("task/delete", view_func=delete_task, methods=["DELETE"])
task_blueprint.add_url_rule("task/get_all_tasks", view_func=get_all_tasks, methods=["GET"])
task_blueprint.add_url_rule("task/get_tasks_by_date_created", view_func=get_tasks_by_date_created, methods=["GET"])
task_blueprint.add_url_rule("task/get_completed_tasks", view_func=get_completed_tasks, methods=["GET"])