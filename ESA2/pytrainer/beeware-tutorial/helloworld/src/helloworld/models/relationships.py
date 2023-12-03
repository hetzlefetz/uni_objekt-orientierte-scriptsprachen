from peewee import ForeignKeyField, IntegerField, DecimalField
from helloworld.models.base_model import BaseModel
from helloworld.models.exercise import Exercise
from helloworld.models.plan import Plan


class ExercisePlan(BaseModel):
    exercise = ForeignKeyField(Exercise)
    plan = ForeignKeyField(Plan)
    reps = IntegerField()
    weights = DecimalField()
