from kink import inject
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from helloworld.services.router import Routes, Router


class Menu:
    @inject
    def __init__(self, router_service: Router):
        self.router = router_service

    def navigateToExercise(self, widget):
        self.router.go(Routes.EXERCISES)

    def navigateToPlan(self, widget):
        self.router.go(Routes.PLANS)

    def navigateToProfiles(self, widget):
        self.router.go(Routes.PROFILES)

    def navigateToWorkout(self, widget):
        self.router.go(Routes.WORKOUT)

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        exercises = toga.Button(
            "Exercises",
            on_press=self.navigateToExercise,
            style=Pack(padding=5),
        )
        profiles = toga.Button(
            "Profiles", on_press=self.navigateToProfiles, style=Pack(padding=5)
        )
        training = toga.Button(
            "Training Plan",
            on_press=self.navigateToPlan,
            style=Pack(padding=5),
        )
        workout = toga.Button(
            "Workouts", on_press=self.navigateToWorkout, style=Pack(padding=5)
        )

        main_box.add(exercises)
        main_box.add(profiles)
        main_box.add(training)
        main_box.add(workout)

        return main_box

    def getName(self) -> str:
        return "Main Menu"
