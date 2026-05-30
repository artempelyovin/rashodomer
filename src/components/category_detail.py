from typing import Callable

import flet as ft

from models import CategoryModel, CategoryType
from ui_utils import show_success
from utils import format_datetime


@ft.component
def CategoryDetail(
    category: CategoryModel,
    on_cancel: Callable,
    on_edit: Callable,
    on_delete: Callable,
) -> ft.Control:
    icon = ft.Icons.ARROW_UPWARD if category.type == CategoryType.INCOME else ft.Icons.ARROW_DOWNWARD
    color = ft.Colors.GREEN if category.type == CategoryType.INCOME else ft.Colors.RED
    type_label = "Доход" if category.type == CategoryType.INCOME else "Расход"

    async def copy_id(_) -> None:
        await ft.Clipboard().set(category.id)
        show_success("ID скопирован")

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Обзор категории", size=24),
                    ft.IconButton(
                        icon=ft.Icons.COPY,
                        tooltip=f"Скопировать ID: {category.id}",
                        on_click=copy_id,
                    ),
                    ft.IconButton(icon=ft.Icons.DELETE, on_click=on_delete),
                ]
            ),
            ft.Row([ft.Text("Название:"), ft.Text(category.name)]),
            ft.Row([ft.Text("Описание:"), ft.Text(category.description or "—")]),
            ft.Row(
                [
                    ft.Text("Тип:"),
                    ft.Icon(icon, color=color),
                    ft.Text(type_label, color=color),
                ]
            ),
            ft.Switch(label="Активна", value=category.is_active, disabled=True),
            ft.Row([ft.Text("Создано:"), ft.Text(format_datetime(category.created_at))]),
            ft.Row([ft.Text("Обновлено:"), ft.Text(format_datetime(category.updated_at))]),
            ft.FloatingActionButton(icon=ft.Icons.EDIT, on_click=on_edit),
        ]
    )
