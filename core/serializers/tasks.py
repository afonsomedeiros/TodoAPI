from marshmallow import Schema, fields, post_load
from core.models import Tasks
from core.serializers import UserSchema
import json


class TaskSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    user = fields.Nested(UserSchema, exclude=["password"])
    is_active = fields.Boolean()
    finished_at = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Tasks(**data)
