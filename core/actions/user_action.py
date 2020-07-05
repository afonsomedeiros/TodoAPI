from bottle import request, response

from core.models import Users
from core.serializers import UserSerializer


def list_user(*args, **kwargs):
    users = list(Users().select().execute())
    schema = UserSerializer(many=True)
    data = schema.dump(users, many=True)
    response.content_type = "application/json"
    return data
