import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject


from helloworld.services.router import Router, Routes
from helloworld.models.exercise import Exercise


class Exercises:
    def navigateToExerciseCreate(self, widget):
        self.router.go(Routes.EXERCISES_CREATE)

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service
        self.exercises = []
        for u in Exercise.select():
            self.exercises.append({"name": u.name})

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Available Exercises", style=Pack(padding=5))
        main_box.add(label)

        for e in self.exercises:
            main_box.add(toga.Label(f"Name: {e['name']}"))
            main_box.add(toga.Divider())

        btn_create = toga.Button(
            "Exercises Create",
            on_press=self.navigateToExerciseCreate,
            style=Pack(padding=5),
        )

        btn_back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )

        main_box.add(btn_create)
        main_box.add(btn_back)

        return main_box

    def getName(self) -> str:
        return "Exercises"
