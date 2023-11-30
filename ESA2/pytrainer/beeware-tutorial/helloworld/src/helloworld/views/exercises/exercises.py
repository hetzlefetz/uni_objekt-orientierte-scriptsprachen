import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.helloService import HelloService
from helloworld.services.routes import Routes


class Exercises:
    def navigateToExerciseCreate(self, widget):
        self.router.go(Routes.EXERCISES_CREATE)

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    @inject
    def __init__(self, router, hello_service: HelloService) -> None:
        self.router = router
        hello_service.sayHello()

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Hello from Exercises")

        create = toga.Button(
            "Exercises Create",
            on_press=self.navigateToExerciseCreate,
            style=Pack(padding=5),
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )

        main_box.add(label)
        main_box.add(create)
        main_box.add(back)

        return main_box

    def getName(self) -> str:
        return "Exercises"
