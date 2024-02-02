import flet as ft

class BlocoNotas:
    def __init__(self):
        pass
def main(page:ft.Page):
    app = BlocoNotas()
    page.add(app)
ft.app(target=main)