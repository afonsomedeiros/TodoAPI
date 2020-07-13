from bottle import request, response
from marshmallow import ValidationError
from core.models import Tasks, Users
from core.serializers import TaskSchema, UserSchema
from core.utils.kit import serializer_error
from peewee import DoesNotExist
import datetime


def list_task(user):
    response.content_type = "application/json"
    schema = TaskSchema(many=True)
    try:
        tasks = Tasks.select().where(Tasks.user==user)
        return schema.dumps(tasks)
    except DoesNotExist as err:
        response.content_type = 404
        return schema.dumps(Tasks(title="Não encontrado", description="Tarefa não localizada ou não existe."))


def view_task(user, task_id):
    response.content_type = "application/json"
    schema = TaskSchema()
    try:
        task = Tasks.get(Tasks.id==task_id, Tasks.user==user)
        return schema.dumps(task)
    except DoesNotExist as err:
        response.status = 404
        return schema.dumps(Tasks(title="Não encontrado",
                                  description="Tarefa não localizada ou não existe.",
                                  user=user,
                                  is_active=False,
                                  finished_at=datetime.date.today()))


def create_task(user):
    response.content_type = "application/json"
    try:
        schema = TaskSchema(partial=True)
        task = schema.load(request.json)
        task.user = user
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        response.status = 417
        return serializer_error(err.messages, err.valid_data)


def update_task(user):
    response.content_type = "application/json"
    try:
        schema = TaskSchema(partial=True)
        task = schema.load(request.json)
        task.user = user
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        response.status = 417
        return serializer_error(err.messages, err.valid_data)
