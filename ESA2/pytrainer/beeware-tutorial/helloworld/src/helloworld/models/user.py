from peewee import CharField, AutoField

from helloworld.models.base_model import BaseModel


class User(BaseModel):
    id = AutoField()
    name = CharField()
    mail = CharField(unique=True)
    pw = CharField()
