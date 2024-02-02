import flet as ft

from appBar import Apbar

class BlocoNotas:
    def __init__(self):
        self.appBar = Apbar()
def main(page:ft.Page):
    app = BlocoNotas()
    page.add(app)
ft.app(target=main)