import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject
from helloworld.services.router import Router, Routes
from helloworld.models.plan import Plan


class Workout:
    def navigateToWorkoutTraining(self, widget):
        self.router.go(Routes.WORKOUT_TRAINING, self.selection.value)

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    def changeItem(self, widget):
        if self.selection.value != "Please choose a Plan...":
            self.btn_start.enabled = True

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service
        self.available_plans = Plan.select()

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Start Workout")

        items = ["Please choose a Plan..."]
        for e in self.available_plans:
            items.append(e.name)
        self.selection = toga.Selection(
            items=items,
            on_select=self.changeItem,
            style=Pack(padding=5),
        )

        self.btn_start = toga.Button(
            "Start selected workout",
            on_press=self.navigateToWorkoutTraining,
            style=Pack(padding=5),
            enabled=False,
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        main_box.add(label)
        main_box.add(self.selection)
        main_box.add(self.btn_start)
        main_box.add(back)
        return main_box

    def getName(self) -> str:
        return "Workout"
