from peewee import CharField, BooleanField, AutoField


from helloworld.models.base_model import BaseModel


class Exercise(BaseModel):
    id = AutoField()
    name = CharField()
    use_weights = BooleanField()
    is_repeatable = BooleanField()
