from data.engine import TimeStampBaseModel
from peewee import CharField, DateTimeField, ForeignKeyField, BooleanField

from .users import Users


class Tasks(TimeStampBaseModel):

    title = CharField(max_length=100)
    description = CharField(max_length=500, null=True)
    user = ForeignKeyField(Users)
    is_active = BooleanField(default=False)
    finished_at = DateTimeField(null=True)