import flet as ft

class Apbar():
    def __init__(self, page:ft.Page):
        self.page = page
        self.appbar = ft.AppBar(
            title=ft.Text("Bloco de notas", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700
        )
        self.page.appbar = self.appbar
        self.page.update()