from typing import Callable

import flet as ft

from models import CategoryType


@ft.component
def CategoryCreate(on_cancel: Callable, on_save: Callable) -> ft.Control:
    name, set_name = ft.use_state("")
    description, set_description = ft.use_state("")
    category_type, set_category_type = ft.use_state(CategoryType.EXPENSE)

    def handle_save():
        on_save(name=name, description=description, category_type=category_type)

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Создание категории", size=24),
                    ft.IconButton(icon=ft.Icons.CHECK, on_click=handle_save),
                ]
            ),
            ft.TextField(
                label="Название",
                value=name,
                on_change=lambda e: set_name(e.control.value),
            ),
            ft.TextField(
                label="Описание",
                value=description,
                on_change=lambda e: set_description(e.control.value),
            ),
            ft.Row(
                [
                    ft.Text("Тип:"),
                    ft.SegmentedButton(
                        selected=[str(category_type)],
                        segments=[
                            ft.Segment(value=CategoryType.EXPENSE, label=ft.Text("Расход")),
                            ft.Segment(value=CategoryType.INCOME, label=ft.Text("Доход")),
                        ],
                        on_change=lambda e: set_category_type(CategoryType(list(e.control.selected)[0])),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
        ]
    )
