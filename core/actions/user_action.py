from bottle import request, response
from marshmallow import ValidationError

from core.models import Users
from core.serializers import UserSchema
from core.utils.kit import serializer_date
import json


def list_user(*args, **kwargs):
    users = Users().select(Users.id, Users.name, Users.last_name,
                           Users.email, Users.birthday, Users.created_at,
                           Users.updated_at).execute()
    schema = UserSchema(many=True)
    data = schema.dump(users, many=True)
    response.content_type = "application/json"
    return data


def view_user(*args, **kwargs):
    user = Users.select(
        Users.id, Users.name, Users.last_name,
        Users.email, Users.birthday, Users.created_at,
        Users.updated_at
    ).where(Users.id == kwargs['user_id']).get()
    schema = UserSchema()
    data = schema.dump(user)
    response.content_type = "application/json"
    return data


def create_user(*args, **kwargs):
    response.content_type = "application/json"
    try:
        post_data = request.json
        schema = UserSchema()
        user = schema.load(post_data)
        user.gen_hash()
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        error_response = {
            'err_messages': err.messages,
            'err_valid_data': err.valid_data
        }
        return json.dumps(error_response, default=serializer_date)


def update_user(*args, **kwargs):
    response.content_type = "application/json"
    try:
        post_data = request.json
        schema = UserSchema()
        user = schema.load(post_data)
        user.save()
        return schema.dump(user)
    except ValidationError as err:
        error_response = {
            'err_messages': err.messages,
            'err_valid_data': err.valid_data
        }
        return json.dumps(error_response, default=serializer_date)
