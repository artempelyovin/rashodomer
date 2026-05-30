from typing import Callable

import flet as ft

from models import BudgetModel
from ui_utils import show_success
from utils import format_datetime


@ft.component
def BudgetDetail(budget: BudgetModel, on_cancel: Callable, on_edit: Callable, on_delete: Callable) -> ft.Control:
    async def copy_id(_) -> None:
        await ft.Clipboard().set(budget.id)
        show_success("ID скопирован")

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Обзор бюджета", size=24),
                    ft.IconButton(
                        icon=ft.Icons.COPY,
                        tooltip=f"Скопировать ID: {budget.id}",
                        on_click=copy_id,
                    ),
                    ft.IconButton(icon=ft.Icons.DELETE, on_click=on_delete),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Название:"),
                    ft.Text(budget.name),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Описание:"),
                    ft.Text(budget.description),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Сумма:"),
                    ft.Text(str(budget.amount)),
                ]
            ),
            ft.Switch(label="Активен", value=budget.is_active, disabled=True),
            ft.Row(
                [
                    ft.Text("Создано:"),
                    ft.Text(value=format_datetime(budget.created_at)),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Обновлено:"),
                    ft.Text(value=format_datetime(budget.updated_at)),
                ]
            ),
            ft.FloatingActionButton(icon=ft.Icons.EDIT, on_click=on_edit),
        ]
    )
