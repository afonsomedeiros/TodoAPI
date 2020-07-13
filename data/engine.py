from peewee import SqliteDatabase, DateTimeField
from playhouse.signals import Model, pre_save
from settings import ROOT_PATH, DATETIME_FORMAT
import datetime


class Base(Model):
    """
        Classe que provê conexão com banco de dados e implementa recursos dos
        Models do peewee.
    """

    class Meta:
        database = SqliteDatabase(f"{ROOT_PATH}/database.db")


class TimeStampBaseModel(Base):
    """
        classe que provê TimeStamp.
    """
    created_at = DateTimeField(formats=DATETIME_FORMAT)
    updated_at = DateTimeField(formats=DATETIME_FORMAT)


@pre_save(sender=TimeStampBaseModel)
def before_save(models_class, instance, created):
    if not instance.id:
        instance.created_at = datetime.datetime.today()
    instance.updated_at = datetime.datetime.today()
