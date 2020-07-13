from marshmallow import Schema, fields, post_load, post_dump
from core.models import Users
from settings import DATE_FORMAT, DATETIME_FORMAT


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.Field()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()
    birthday = fields.Date(format=DATE_FORMAT)
    created_at = fields.DateTime(format=DATETIME_FORMAT)
    updated_at = fields.DateTime(format=DATETIME_FORMAT)

    @post_load
    def make_user(self, data, **kwargs):
        return Users(**data)

