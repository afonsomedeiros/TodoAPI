from data.engine import TimeStampBaseModel
from peewee import CharField, DateTimeField, ForeignKeyField

from .users import Users


class Tasks(TimeStampBaseModel):

    title = CharField(max_length=100)
    description = CharField(max_length=500)
    user = ForeignKeyField(Users)
    finished_at = DateTimeField()
