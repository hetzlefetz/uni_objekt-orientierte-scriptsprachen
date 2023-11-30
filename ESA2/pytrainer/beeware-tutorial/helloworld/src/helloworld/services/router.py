import toga
from helloworld.services.routes import Routes
from helloworld.views.exercises.exercises_create import ExercisesCreate
from helloworld.views.plan.plans import Plans
from helloworld.views.plan.plans_create import PlansCreate
from helloworld.views.profiles.profiles import Profiles
from helloworld.views.profiles.profiles_create import ProfilesCreate
from helloworld.views.workout.workout import Workout
from helloworld.views.workout.workout_training import WorkoutTraining
from helloworld.views.workout.workout_training_detail import (
    WorkoutTrainingDetail,
)
from helloworld.views.workout.workout_what import WorkoutWhat
from helloworld.views.workout.workout_who import WorkoutWho
from helloworld.views.exercises.exercises import Exercises
from helloworld.views.menu import Menu


class Router:
    routes = {
        Routes.MENU: Menu,
        Routes.EXERCISES: Exercises,
        Routes.EXERCISES_CREATE: ExercisesCreate,
        Routes.PLANS: Plans,
        Routes.PLANS_CREATE: PlansCreate,
        Routes.PROFILES: Profiles,
        Routes.PROFILES_CREATE: ProfilesCreate,
        Routes.WORKOUT: Workout,
        Routes.WORKOUT_WHO: WorkoutWho,
        Routes.WORKOUT_WHAT: WorkoutWhat,
        Routes.WORKOUT_TRAINING: WorkoutTraining,
        Routes.WORKOUT_TRAINING_DETAIL: WorkoutTrainingDetail,
    }

    def __init__(self, mainWindow: toga.MainWindow):
        self.rootWindow = mainWindow

    def go(self, where):
        instance = self.routes[where](self)
        self.rootWindow.title = instance.getName()
        self.rootWindow.content = instance.getContent()
