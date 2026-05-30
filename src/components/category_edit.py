from typing import Callable

import flet as ft

from models import CategoryModel, CategoryType
from utils import format_datetime


@ft.component
def CategoryEdit(
    category: CategoryModel,
    on_cancel: Callable,
    on_save: Callable,
) -> ft.Control:
    name, set_name = ft.use_state(category.name)
    description, set_description = ft.use_state(category.description)
    category_type, set_category_type = ft.use_state(category.type)
    is_active, set_is_active = ft.use_state(category.is_active)

    def handle_save() -> None:
        on_save(
            category_id=category.id,
            name=name,
            description=description,
            category_type=category_type,
            is_active=is_active,
        )

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Редактирование категории", size=24),
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
            ft.Switch(
                label="Активна",
                value=is_active,
                on_change=lambda e: set_is_active(e.control.value),
            ),
            ft.Row([ft.Text("Создано:"), ft.Text(format_datetime(category.created_at))]),
            ft.Row([ft.Text("Обновлено:"), ft.Text(format_datetime(category.updated_at))]),
        ]
    )
