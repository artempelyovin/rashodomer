from datetime import datetime
from decimal import Decimal

import flet as ft
from flet import Control

from src.models import BudgetModel
from src.utils import format_datetime


@ft.component
def BudgetEdit() -> Control:
    params = ft.use_route_params()
    budget_id = params.get("budget_id")
    budget = BudgetModel(
        id=budget_id,
        name="Наличные/карты",
        description="Все деньги на руках (наличные/карты)",
        amount=Decimal(10000),
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return ft.Column(
        controls=[
            ft.Text("Редактирование бюджета", size=24),
            ft.Row(
                controls=[
                    ft.Text("ID:"),
                    ft.Text(budget_id),
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
