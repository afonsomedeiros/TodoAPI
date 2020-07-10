from data.engine import TimeStampBaseModel
from peewee import CharField, DateTimeField, ForeignKeyField, BooleanField

from .users import Users


class Tasks(TimeStampBaseModel):

    title = CharField(max_length=100)
    description = CharField(max_length=500)
    user = ForeignKeyField(Users)
    is_active = BooleanField()
    finished_at = DateTimeField()