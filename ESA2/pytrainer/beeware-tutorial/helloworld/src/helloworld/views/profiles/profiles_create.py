import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from kink import inject


from helloworld.services.router import Router, Routes
from helloworld.models.user import User


class ProfilesCreate:
    def navigateBack(self, widget):
        self.router.go(Routes.PROFILES)

    def createProfile(self, widget):
        profile = User(
            name=self.txt_name.value,
            mail=self.txt_mail.value,
            pw=self.txt_pw.value,
        )
        profile.save()
        self.router.go(Routes.PROFILES)

    @inject
    def __init__(self, router_service: Router) -> None:
        self.router = router_service

    def getContent(self) -> toga.Box:
        main_box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Create your Profile")

        self.txt_name = toga.TextInput(placeholder="Name")
        self.txt_mail = toga.TextInput(placeholder="Mail")
        self.txt_pw = toga.PasswordInput(placeholder="Password")

        btn_create = toga.Button(
            "Create", on_press=self.createProfile, style=Pack(padding=5)
        )
        btn_back = toga.Button(
            "Back", on_press=self.navigateBack, style=Pack(padding=5)
        )
        main_box.add(label)
        main_box.add(self.txt_name)
        main_box.add(self.txt_mail)
        main_box.add(self.txt_pw)
        main_box.add(btn_create)
        main_box.add(btn_back)
        return main_box

    def getName(self) -> str:
        return "Profiles Create"
