import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.helloService import HelloService


class WorkoutTrainingDetail:
    @inject
    def __init__(self, router, hello_service: HelloService) -> None:
        self.router = router
        hello_service.sayHello()

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Hello from Workout Training Detail")
        main_box.add(label)
        return main_box

    def getName(self) -> str:
        return "Workout Training Detail"
