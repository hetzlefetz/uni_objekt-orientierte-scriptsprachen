from peewee import SqliteDatabase
from toga import App


from helloworld.models.user import User
from helloworld.models.exercise import Exercise
from helloworld.models.plan import Plan
from helloworld.models.relationships import ExercisePlan


class SqliteDbService:
    initialized = False
    db = None

    def setup(self, app: App):
        self.db = SqliteDatabase("helloworld.db")
        self.db.connect()
        # self.db.drop_tables([User, ExercisePlan, Plan])
        self.db.create_tables([User, Exercise, Plan, ExercisePlan], safe=True)
        self.initialized = True
