from kink import inject
import toga

from helloworld.services.router import Router, Routes
from helloworld.services.sqlite_db_service import SqliteDbService
from helloworld.views.plan.plans_add import PlansAdd
from helloworld.views.exercises.exercises_create import ExercisesCreate
from helloworld.views.plan.plans import Plans
from helloworld.views.plan.plans_create import PlansCreate
from helloworld.views.profiles.profiles import Profiles
from helloworld.views.profiles.profiles_create import ProfilesCreate
from helloworld.views.workout.workout import Workout
from helloworld.views.workout.workout_training import WorkoutTraining
from helloworld.views.workout.workout_training_finish import (
    WorkoutTrainingFinished,
)

from helloworld.views.exercises.exercises import Exercises
from helloworld.views.menu import Menu


class app(toga.App):
    @inject
    def __init__(
        self,
        router_service: Router,
        db_service: SqliteDbService,
        formal_name=None,
        app_id=None,
        app_name=None,
        id=None,
        icon=None,
        author=None,
        version=None,
        home_page=None,
        description=None,
        startup=None,
        windows=None,
        on_exit=None,
        factory=None,
    ):
        super().__init__(
            formal_name,
            app_id,
            app_name,
            id,
            icon,
            author,
            version,
            home_page,
            description,
            startup,
            windows,
            on_exit,
            factory,
        )
        self.router = router_service
        self.db = db_service

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = toga.Box()
        self.main_window.show()
        # setup services that need the toga instance
        routes = {
            "menu": Menu,
            "exercises": Exercises,
            "exercises_create": ExercisesCreate,
            "plans": Plans,
            "plans_create": PlansCreate,
            "plans_add": PlansAdd,
            "profiles": Profiles,
            "profiles_create": ProfilesCreate,
            "workout": Workout,
            "workout_training": WorkoutTraining,
            "workout_training_detail": WorkoutTrainingFinished,
        }

        self.router.setup(self.main_window, routes)
        self.db.setup(self)

        # start the actual app
        self.router.go(Routes.MENU)


def main():
    return app()
