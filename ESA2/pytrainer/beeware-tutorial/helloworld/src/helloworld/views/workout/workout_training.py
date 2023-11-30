import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.helloService import HelloService
from helloworld.services.routes import Routes


class WorkoutTraining:
    def navigateToWorkoutTrainingDetail(self, widget):
        self.router.go(Routes.WORKOUT_TRAINING_DETAIL)

    def navigateBack(self, widget):
        self.router.go(Routes.WORKOUT_WHAT)

    @inject
    def __init__(self, router, hello_service: HelloService) -> None:
        self.router = router
        hello_service.sayHello()

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Hello from Workout Training")
        trainingDetail = toga.Button(
            "Detail",
            on_press=self.navigateToWorkoutTrainingDetail,
            style=Pack(padding=5),
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        main_box.add(label)
        main_box.add(trainingDetail)
        main_box.add(back)
        return main_box

    def getName(self) -> str:
        return "Workout Training"
