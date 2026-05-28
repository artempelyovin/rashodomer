import flet as ft


def Error(message: str) -> ft.Control:
    return ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.ERROR),
                ft.Text(message),
            ],
        ),
        bgcolor=ft.Colors.RED_400,
        duration=3000,
    )
