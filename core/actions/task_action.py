from bottle import request, response
from marshmallow import ValidationError

from core.models import Tasks, Users
from core.serializers import TaskSchema, UserSchema
from core.utils.kit import serializer_error, remove_password


def list_task():
    tasks = remove_password(Tasks.select())
    schema = TaskSchema(many=True)
    response.content_type = "application/json"
    return schema.dumps(tasks)


def view_task(*args, **kwargs):
    task = remove_password([Tasks.get(Tasks.id==kwargs['task_id'])])[0]
    schema = TaskSchema()
    response.content_type = "application/json"
    return schema.dumps(task)


def create_task():
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
        task.user = remove_password([Users.get_by_id(user_id)])[0]
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
        task = remove_password([task])[0]
        return schema.dumps(task)
    except ValidationError as err:
        response.status_code = 417
        return serializer_error(err.messages, err.valid_data)