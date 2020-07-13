from bottle import request, response

from marshmallow import ValidationError

from core.models import Users
from core.serializers import UserSchema
from core.utils.kit import serializer_error


def view_user(user):
    schema = UserSchema()
    data = schema.dump(user)
    response.content_type = "application/json"
    return data


def create_user():
    response.content_type = "application/json"
    try:
        schema = UserSchema()
        user = schema.load(request.json)
        user.gen_hash()
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        return serializer_error(err.messages, err.valid_data)


def update_user(user):
    response.content_type = "application/json"
    try:
        schema = UserSchema()
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        return serializer_error(err.messages, err.valid_data)
