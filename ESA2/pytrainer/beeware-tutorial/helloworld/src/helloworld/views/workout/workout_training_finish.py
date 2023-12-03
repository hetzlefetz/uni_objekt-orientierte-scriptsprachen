import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Router, Routes


class WorkoutTrainingFinished:
    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Congratulations you finished your training")
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        main_box.add(label)
        main_box.add(back)
        return main_box

    def getName(self) -> str:
        return "Workout Training Finished"
