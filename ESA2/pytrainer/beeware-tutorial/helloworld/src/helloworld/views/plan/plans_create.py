import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Router, Routes
from helloworld.models.exercise import Exercise
from helloworld.models.plan import Plan
from helloworld.models.relationships import ExercisePlan


class PlansCreate:
    def on_change_name(self, widget):
        if len(self.txt_title.value) > 0:
            self.save_button.enabled = True

    def savePlan(self, widget):
        plan = Plan(name=self.txt_title.value)
        plan.save()
        for e in self.exercises_added:
            ep = ExercisePlan(
                exercise=e["id"],
                plan=plan.id,
                reps=e["reps"],
                weights=e["weight"],
            )
            ep.save()

        self.router.go(Routes.PLANS)

    def navigateBack(self, widget):
        self.router.go(Routes.PLANS)

    def addExercise(self, widget):
        self.router.go(
            Routes.PLANS_ADD, self.selected_item, self.exercises_added
        )

    def changeItem(self, widget):
        self.selected_item = None

        for e in self.exercises_available:
            if e.name == self.selection.value:
                self.selected_item = e

        self.add_button.enabled = True

    @inject
    def __init__(self, router_service: Router, chosen) -> None:
        self.router = router_service
        self.exercises_available = Exercise.select()
        self.exercises_added = [] if chosen is None else chosen

    def getContent(self) -> toga.Box:
        self.exercises_list = toga.Box(style=Pack(direction=COLUMN))
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Add Exercises to your training plan")
        self.back_button = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        self.main_box.add(toga.Label(text="Name of the plan:"))
        self.txt_title = toga.TextInput(
            placeholder="Name", on_change=self.on_change_name
        )
        self.main_box.add(self.txt_title)
        items = ["Please choose an Exercise ..."]
        for e in self.exercises_available:
            items.append(e.name)
        self.selection = toga.Selection(
            items=items,
            on_select=self.changeItem,
            style=Pack(padding=5),
        )
        self.save_button = toga.Button(
            text="Save",
            on_press=self.savePlan,
            enabled=len(self.exercises_added) > 0
            and len(self.txt_title.value) > 0,
        )

        self.add_button = toga.Button(
            text="Add",
            on_press=self.addExercise,
            enabled=False,
        )

        self.main_box.add(label)
        self.main_box.add(self.selection)
        self.main_box.add(self.add_button)
        self.main_box.add(self.save_button)
        self.main_box.add(self.back_button)
        self.addList(self.exercises_added)

        return self.main_box

    def getName(self) -> str:
        return "Plan Create"

    def addList(self, exercises):
        self.main_box.add(toga.Label(text="Already added:"))
        self.exercises_list = toga.Box(style=Pack(direction=COLUMN))
        for e in exercises:
            self.exercises_list.add(toga.Label(text=e["name"]))

        self.main_box.add(self.exercises_list)
