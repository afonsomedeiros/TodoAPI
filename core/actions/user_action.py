from bottle import request, response

from marshmallow import ValidationError

from core.models import Users
from core.serializers import UserSchema
from core.utils.kit import serializer_error


def view_user(user):
    """Visualiza informações sobre usuário Logado.

    Args:
        user (Peewee Model): Classe que trará informações do banco de dados.

    Returns:
        str: Usuário serializado com as informações necessárias.
    """
    schema = UserSchema(exclude=['password'])
    data = schema.dump(user)
    response.content_type = "application/json"
    return data


def create_user():
    """Cadatrar usuários.

    Returns:
        str: Retorna dados dos usuários cadastrados.
    """
    response.content_type = "application/json"
    try:
        schema = UserSchema(exclude=['password'])
        user = schema.load(request.json)
        user.gen_hash()
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        return serializer_error(err.messages, err.valid_data)


def update_user(user):
    """atualizar dados dos usuários.

    Args:
        user (Peewee Model): Classe que abstrai tabela de usuários do banco.

    Returns:
        str: Retorna dados dos usuários atualizados.
    """
    response.content_type = "application/json"
    try:
        schema = UserSchema(exclude=['password'])
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        return serializer_error(err.messages, err.valid_data)
