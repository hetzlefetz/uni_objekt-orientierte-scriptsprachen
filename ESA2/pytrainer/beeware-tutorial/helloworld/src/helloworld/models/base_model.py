from peewee import Model, SqliteDatabase

db = SqliteDatabase("helloworld.db")


class BaseModel(Model):
    class Meta:
        database = db
