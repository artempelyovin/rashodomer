from datetime import datetime
from decimal import Decimal

import flet as ft
from flet import Control

from src.models import BudgetModel
from src.utils import format_datetime


class BudgetDetailedForm(ft.Column):
    def __init__(self, budget: BudgetModel):
        super().__init__()
        self.budget = budget
        self.controls = self.build_controls()

    def build_controls(self) -> list[Control]:
        return [
            ft.Text("Редактирование бюджета", size=24),
            ft.TextField(label="Название", value=self.budget.name),
            ft.TextField(label="Описание", value=self.budget.description),
            ft.TextField(
                value=str(self.budget.amount),
                label="Сумма",
                hint_text="0.00",
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$", allow=True),
                text_align=ft.TextAlign.RIGHT,  # суммы обычно выравнивают по правому краю
            ),
            ft.Switch(label="Архивирован", value=self.budget.is_active),
            ft.Row(
                [
                    ft.Text("Создано:"),
                    ft.Text(value=format_datetime(self.budget.updated_at)),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Обновлено:"),
                    ft.Text(value=format_datetime(self.budget.updated_at)),
                ]
            ),
        ]


def main(page: ft.Page):
    page.title = "Flet + ViewModel"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.window_width = 600
    page.window_height = 700
    budget = BudgetModel(
        id="f0322c21-8a6a-41df-8847-c82ddcc7a095",
        name="Наличные/карты",
        description="Все деньги на руках (наличные/карты)",
        amount=Decimal(10000),
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    form = BudgetDetailedForm(budget=budget)
    page.add(form)


ft.app(target=main)
