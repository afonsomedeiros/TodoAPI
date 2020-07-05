from marshmallow import Schema, fields, post_load, post_dump
from core.models import Users
import json


class UserSerializer(Schema):
    name = fields.Field()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()
    birthday = fields.Date()

    @post_load
    def make_user(self, data, **kwargs):
        return Users(**data)

    @post_dump(pass_many=True)
    def correct_serializer(self, data, many, **kwargs):
        return json.dumps(str(data), ensure_ascii=False)
