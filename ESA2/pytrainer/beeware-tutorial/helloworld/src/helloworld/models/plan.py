from peewee import CharField, AutoField

from helloworld.models.base_model import BaseModel


class Plan(BaseModel):
    id = AutoField()
    name = CharField(unique=True)
