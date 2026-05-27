import flet as ft
from flet import run


def main(page: ft.Page):
    page.title = "Пример транзакции"

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.ADD_CARD),
                    ft.Column(
                        controls=[ft.Text("Закупился в sds"), ft.Text("Еда и напитки")]
                    ),
                    ft.Text("128$"),
                ]
            )
        ),
        ft.FloatingActionButton(icon=ft.Icons.ADD),
    )


if __name__ == "__main__":
    run(main)
