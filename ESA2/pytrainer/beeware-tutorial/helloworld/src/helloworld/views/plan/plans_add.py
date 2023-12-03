import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Router, Routes


class PlansAdd:
    def addExercise(self, widget):
        self.chosen.append(
            {
                "id": self.selected_item.id,
                "name": self.selected_item.name,
                "reps": -1
                if not self.selected_item.is_repeatable
                else self.weightValue.value,
                "weight": -1
                if not self.selected_item.use_weights
                else self.weightValue.value,
            }
        )
        print(self.chosen)
        self.router.go(Routes.PLANS_CREATE, self.chosen)

    def cancel(self, widget):
        self.router.go(Routes.PLANS_CREATE, self.chosen)

    @inject
    def __init__(self, router_service: Router, exercise, chosen) -> None:
        self.selected_item = exercise
        self.chosen = chosen
        self.router = router_service

    def getContent(self) -> toga.Box:
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_box.add(
            toga.Label(text=f"Adding Exercise: {self.selected_item.name}")
        )
        self.weightValue = toga.NumberInput()
        self.repValue = toga.NumberInput()
        if self.selected_item.use_weights:
            self.main_box.add(toga.Label(text="How much weight?"))
            self.main_box.add(self.weightValue)
        if self.selected_item.is_repeatable:
            self.main_box.add(toga.Label(text="How many repetitions?"))
            self.main_box.add(self.repValue)

        self.main_box.add(toga.Button(text="Add", on_press=self.addExercise))
        self.main_box.add(toga.Button(text="Cancel", on_press=self.cancel))
        return self.main_box

    def getName(self) -> str:
        return "Plan Add"
