import datetime

from marshmallow import Schema, fields, post_load, pre_dump
from core.models import Tasks
from core.serializers import UserSchema
from settings import DATETIME_FORMAT


class TaskSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    user = fields.Nested(UserSchema, exclude=["password"])
    is_active = fields.Boolean()
    finished_at = fields.DateTime(format=DATETIME_FORMAT, required=False)
    created_at = fields.DateTime(format=DATETIME_FORMAT, required=False)
    updated_at = fields.DateTime(format=DATETIME_FORMAT, required=False)

    @post_load
    def make_user(self, data, **kwargs):
        return Tasks(**data)