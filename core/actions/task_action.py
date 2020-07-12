from bottle import request, response
from marshmallow import ValidationError
from core.models import Tasks, Users
from core.serializers import TaskSchema, UserSchema
from core.utils.kit import serializer_error


def list_task():
    tasks = Tasks.select()
    schema = TaskSchema(many=True)
    response.content_type = "application/json"
    return schema.dumps(tasks)


def view_task(*args, **kwargs):
    task = Tasks.get(Tasks.id==kwargs['task_id'])
    schema = TaskSchema()
    response.content_type = "application/json"
    return schema.dumps(task)


def create_task(*args, **kwargs):
    """
        Alterar a forma de autenticacao de usuário para utilizar usuario da sessao.

    """
    response.content_type = "application/json"
    try:
        post_data = request.json
        user_id = post_data['user']
        post_data['user'] = {}
        schema = TaskSchema(partial=True)
        task = schema.load(post_data)
        task.user = Users.get_by_id(user_id)
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        response.status_code = 417
        return serializer_error(err.messages, err.valid_data)


def update_task():
    """
        Alterar a forma de autenticacao de usuário para utilizar usuario da sessao.
    """
    response.content_type = "application/json"
    try:
        post_data = request.json
        schema = TaskSchema(partial=True)
        task_aux = Tasks.get_by_id(post_data['id'])
        task = schema.load(post_data)
        task.user = task_aux.user
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        response.status_code = 417
        return serializer_error(err.messages, err.valid_data)