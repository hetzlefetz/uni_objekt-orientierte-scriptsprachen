import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject
from peewee import fn

from helloworld.services.router import Router, Routes
from helloworld.models.plan import Plan
from helloworld.models.exercise import Exercise
from helloworld.models.relationships import ExercisePlan


class Plans:
    def navigateToPlansCreate(self, widget):
        self.router.go(Routes.PLANS_CREATE, [])

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service
        self.available_plans = Plan.select()

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))

        if not self.available_plans is None:
            label = toga.Label("Available Plans:")
            main_box.add(label)
            for plan in self.available_plans:
                query = (
                    ExercisePlan.select(fn.Count("id"))
                    .where(ExercisePlan.plan == plan.id)
                    .count()
                )
                main_box.add(
                    toga.Label(
                        text=f"Plan {plan.name} with {query} exercise(s)"
                    )
                )
        else:
            label = toga.Label("Create a Plan using 'Plans Create'")
            main_box.add(label)

        create = toga.Button(
            "Plans Create",
            on_press=self.navigateToPlansCreate,
            style=Pack(padding=5),
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )

        main_box.add(create)
        main_box.add(back)

        return main_box

    def getName(self) -> str:
        return "Plans"
