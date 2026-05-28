import flet as ft

from components.error import Error


def show_error(message: str) -> None:
    ft.context.page.show_dialog(Error(message))
