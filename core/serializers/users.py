from marshmallow import Schema, fields, post_load, post_dump
from core.models import Users
import json


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.Field()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()
    birthday = fields.Date()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Users(**data)

    """@post_dump(pass_many=True)
    def correct_serializer(self, data, many, **kwargs):
        return json.dumps(data, ensure_ascii=False)"""
