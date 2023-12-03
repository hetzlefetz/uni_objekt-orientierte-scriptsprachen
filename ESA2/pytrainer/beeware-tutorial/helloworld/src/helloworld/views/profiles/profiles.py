import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject

from helloworld.services.router import Router, Routes
from helloworld.models.user import User


class Profiles:
    def navigateToProfileCreate(self, widget):
        self.router.go(Routes.PROFILES_CREATE)

    def navigateBack(self, widget):
        self.router.go(Routes.MENU)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service
        self.userData = []
        for u in User.select():
            self.userData.append({"name": u.name, "mail": u.mail})

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label(
            "Currently Available Profiles", style=Pack(padding=5)
        )
        main_box.add(label)

        for u in self.userData:
            main_box.add(toga.Label(f"Name: {u['name']}"))
            main_box.add(toga.Label(f"Mail: {u['mail']}"))
            main_box.add(toga.Divider())

        create = toga.Button(
            "Profile Create",
            on_press=self.navigateToProfileCreate,
            style=Pack(padding=5),
        )
        back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )

        main_box.add(create)
        main_box.add(back)
        return main_box

    def getName(self) -> str:
        return "Profiles"
