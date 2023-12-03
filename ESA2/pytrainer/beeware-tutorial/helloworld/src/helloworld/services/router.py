import toga


from enum import StrEnum


class Routes(StrEnum):
    MENU = "menu"
    EXERCISES = "exercises"
    EXERCISES_CREATE = "exercises_create"
    PLANS = "plans"
    PLANS_CREATE = "plans_create"
    PLANS_ADD = "plans_add"
    PROFILES = "profiles"
    PROFILES_CREATE = "profiles_create"
    WORKOUT = "workout"
    WORKOUT_WHO = "workout_who"
    WORKOUT_WHAT = "workout_what"
    WORKOUT_TRAINING = "workout_training"
    WORKOUT_TRAINING_DETAIL = "workout_training_detail"


class Router:
    def setup(self, mainWindow: toga.MainWindow, routes):
        self.rootWindow = mainWindow
        self.routes = routes

    def go(self, where, *argv):
        instance = self.routes[where](self, *argv)
        self.rootWindow.title = instance.getName()
        self.rootWindow.content = instance.getContent()
