import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Router, Routes
from helloworld.models.exercise import Exercise
from helloworld.models.plan import Plan
from helloworld.models.relationships import ExercisePlan


class WorkoutTraining:
    def navigateToWorkoutTrainingDetail(self, widget):
        self.router.go(Routes.WORKOUT_TRAINING_DETAIL)

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    def selected(self, widget):
        all_done = True
        for c in self.main_box.children:
            if isinstance(c, toga.Switch):
                if not c.value:
                    all_done = False

        if all_done:
            self.btn_finishTraining.enabled = True

    @inject
    def __init__(self, router_service: Router, workout) -> None:
        self.router = router_service
        self.selectedWorkout = Plan.select().where(Plan.name == workout).get()

        self.exercises = (
            Exercise.select()
            .join(ExercisePlan)
            .join(Plan)
            .where(Plan.id == self.selectedWorkout.id)
        )

    def getContent(self) -> toga.Box:
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Hello from Workout Training")
        self.btn_finishTraining = toga.Button(
            "Finish Training",
            on_press=self.navigateToWorkoutTrainingDetail,
            enabled=False,
            style=Pack(padding=5),
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        self.main_box.add(label)

        for e in self.exercises:
            text = e.name
            exercisesPlan = ExercisePlan.select().where(
                ExercisePlan.plan == 1 & ExercisePlan.exercise == e.id
            )
            ep = exercisesPlan.get()
            if e.use_weights:
                text += f" {ep.weights}kg "

            if e.is_repeatable:
                text += f" {ep.reps} "
                text += "Times "

            self.main_box.add(toga.Switch(text=text, on_change=self.selected))

        self.main_box.add(self.btn_finishTraining)
        self.main_box.add(back)
        return self.main_box

    def getName(self) -> str:
        return "Workout Training"
