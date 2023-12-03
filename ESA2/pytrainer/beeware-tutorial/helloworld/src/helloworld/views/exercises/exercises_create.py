import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Routes, Router
from helloworld.models.exercise import Exercise


class ExercisesCreate:
    def navigateBack(self, widget):
        self.router.go(Routes.EXERCISES)

    def createExercise(self, widget):
        exercise = Exercise(
            name=self.txt_name.value,
            use_weights=self.bln_useWeights.value,
            is_repeatable=self.bln_isRepeatable.value,
        )
        exercise.save()
        self.router.go(Routes.EXERCISES)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Create a new Excercise")

        self.txt_name = toga.TextInput(placeholder="name")
        self.bln_useWeights = toga.Switch(text="Use Weights?", value=True)
        self.bln_isRepeatable = toga.Switch(
            text="Is this exercise repeatable?", value=True
        )

        btn_create = toga.Button(
            "Create", on_press=self.createExercise, style=Pack(padding=5)
        )
        btn_back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        main_box.add(label)
        main_box.add(self.txt_name)
        main_box.add(self.bln_useWeights)
        main_box.add(self.bln_isRepeatable)
        main_box.add(btn_create)
        main_box.add(btn_back)
        return main_box

    def getName(self) -> str:
        return "Exercises Create"
