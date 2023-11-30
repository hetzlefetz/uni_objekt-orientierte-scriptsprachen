import toga

from helloworld.services.router import Router, Routes


class app(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = toga.Box()
        self.main_window.show()
        r = Router(self.main_window)
        r.go(Routes.MENU)


def main():
    return app()
