from bottle import request, response
from marshmallow import ValidationError
from core.models import Tasks, Users
from core.serializers import TaskSchema, UserSchema
from core.utils.kit import serializer_error
from peewee import DoesNotExist
import datetime


def list_task(user):
    """Listar tarefas para usuário logado com token ativo.

    Args:
        user (Peewee Model): Classe que abstrai usuarios do banco de dados.

    Returns:
        str: Retorna lista de tarefas de determinado usuário.
    """
    response.content_type = "application/json"
    schema = TaskSchema(many=True)
    try:
        tasks = Tasks.select().where(Tasks.user==user)
        return schema.dumps(tasks)
    except DoesNotExist as err:
        print(err)
        response.content_type = 404
        return schema.dumps(Tasks(title="Não encontrado",
                                  description="Tarefa não localizada ou não existe.",
                                  user=user,
                                  is_active=False,
                                  finished_at=datetime.date.today()))


def list_active(user):
    """Listar tarefas ativas para usuário logado com token ativo.

    Args:
        user (Peewee Model): Classe que abstrai usuarios do banco de dados.

    Returns:
        str: Retorna lista de tarefas de determinado usuário.
    """
    response.content_type = "application/json"
    schema = TaskSchema(many=True)
    try:
        tasks = Tasks.select().where(Tasks.user==user, Tasks.is_active==True)
        return schema.dumps(tasks)
    except DoesNotExist as err:
        print(err)
        response.content_type = 404
        return schema.dumps(Tasks(title="Não encontrado",
                                  description="Tarefa não localizada ou não existe.",
                                  user=user,
                                  is_active=False,
                                  finished_at=datetime.date.today()))


def list_closed(user):
    """Listar tarefas fechadas para usuário logado com token ativo.

    Args:
        user (Peewee Model): Classe que abstrai usuarios do banco de dados.

    Returns:
        str: Retorna lista de tarefas de determinado usuário.
    """
    response.content_type = "application/json"
    schema = TaskSchema(many=True)
    try:
        tasks = Tasks.select().where(Tasks.user==user, Tasks.is_active==False)
        return schema.dumps(tasks)
    except DoesNotExist as err:
        print(err)
        response.content_type = 404
        return schema.dumps(Tasks(title="Não encontrado",
                                  description="Tarefa não localizada ou não existe.",
                                  user=user,
                                  is_active=False,
                                  finished_at=datetime.date.today()))


def view_task(user, task_id):
    """Visualizar tarefa especifica.

    Args:
        user (Peewee Model): Classe que abstrai usuários no banco de dados.
        task_id (int): Identificador de tarefa.

    Returns:
        str: Retorna dados da tarefa especifica.
    """
    response.content_type = "application/json"
    schema = TaskSchema()
    try:
        task = Tasks.get(Tasks.id==task_id, Tasks.user==user)
        return schema.dumps(task)
    except DoesNotExist as err:
        print(err)
        response.status = 404
        return schema.dumps(Tasks(title="Não encontrado",
                                  description="Tarefa não localizada ou não existe.",
                                  user=user,
                                  is_active=False,
                                  finished_at=datetime.date.today()))


def create_task(user):
    """cadastrar nova tarefa para usuário logado.

    Args:
        user (Peewee Model): Classe que abstrai usuários do banco.

    Returns:
        str: Retorna dados da tarefa cadastrada.
    """
    response.content_type = "application/json"
    try:
        schema = TaskSchema(partial=True)
        task = schema.load(request.json)
        task.user = user
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        print(err)
        response.status = 417
        return serializer_error(err.messages, err.valid_data)


def update_task(user):
    """Atualizar tarefa.

    Args:
        user (Peewee Model): Classe que abstrai usuários no banco de dados

    Returns:
        str: Retorna dados atualizados da tarefa.
    """
    response.content_type = "application/json"
    try:
        schema = TaskSchema(partial=True)
        task = schema.load(request.json)
        task.user = user
        task.save()
        return schema.dumps(task)
    except ValidationError as err:
        print(err)
        response.status = 417
        return serializer_error(err.messages, err.valid_data)
