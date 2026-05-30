import flet as ft


def show_error(message: str) -> None:
    ft.context.page.show_dialog(
        ft.SnackBar(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.ERROR),
                    ft.Text(message),
                ],
            ),
            bgcolor=ft.Colors.RED_400,
            duration=3000,
        )
    )


def show_success(message: str) -> None:
    ft.context.page.show_dialog(
        ft.SnackBar(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.CHECK_CIRCLE),
                    ft.Text(message),
                ],
            ),
            bgcolor=ft.Colors.GREEN_400,
            duration=2000,
        )
    )
