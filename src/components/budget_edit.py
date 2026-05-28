from typing import Callable

import flet as ft

from src.models import BudgetModel
from src.utils import format_datetime


def BudgetEdit(budget: BudgetModel, on_cancel: Callable) -> ft.Control:
    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Редактирование бюджета", size=24),
                    ft.IconButton(icon=ft.Icons.CHECK),  # TODO: callback
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("ID:"),
                    ft.Text(budget.id),
                ]
            ),
            ft.TextField(label="Название", value=budget.name),
            ft.TextField(label="Описание", value=budget.description),
            ft.TextField(
                value=str(budget.amount),
                label="Сумма",
                hint_text="0.00",
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$", allow=True),
                text_align=ft.TextAlign.RIGHT,  # суммы обычно выравнивают по правому краю
            ),
            ft.Switch(label="Архивирован", value=budget.is_active),
            ft.Row(
                [
                    ft.Text("Создано:"),
                    ft.Text(value=format_datetime(budget.updated_at)),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Обновлено:"),
                    ft.Text(value=format_datetime(budget.updated_at)),
                ]
            ),
        ]
    )
