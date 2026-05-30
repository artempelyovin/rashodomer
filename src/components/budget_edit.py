from typing import Callable

import flet as ft

from src.models import BudgetModel
from src.utils import format_datetime


@ft.component
def BudgetEdit(budget: BudgetModel, on_cancel: Callable, on_save: Callable) -> ft.Control:
    name, set_name = ft.use_state(budget.name)
    description, set_description = ft.use_state(budget.description)
    amount, set_amount = ft.use_state(budget.amount)
    is_active, set_is_active = ft.use_state(budget.is_active)

    def handle_save() -> None:
        on_save(budget_id=budget.id, name=name, description=description, amount=amount, is_active=is_active)

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Редактирование бюджета", size=24),
                    ft.IconButton(icon=ft.Icons.CHECK, on_click=handle_save),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Text("ID:"),
                    ft.Text(budget.id),
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
            ft.TextField(
                value=str(amount),
                label="Сумма",
                hint_text="0.00",
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$", allow=True),
                text_align=ft.TextAlign.RIGHT,
                on_change=lambda e: set_amount(e.control.value),
            ),
            ft.Switch(
                label="Активен",
                value=is_active,
                on_change=lambda e: set_is_active(e.control.value),
            ),
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
