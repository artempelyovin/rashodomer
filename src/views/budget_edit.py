import flet as ft
from flet import Control

from src.models import BudgetModel
from src.utils import format_datetime


class BudgetEditView(ft.View):
    def __init__(self, budget: BudgetModel):
        super().__init__()
        self.budget = budget
        self.controls = self.build_controls()

    def build_controls(self) -> list[Control]:
        return [
            ft.Column(
                controls=[
                    ft.Text("Редактирование бюджета", size=24),
                    ft.TextField(label="Название", value=self.budget.name),
                    ft.TextField(label="Описание", value=self.budget.description),
                    ft.TextField(
                        value=str(self.budget.amount),
                        label="Сумма",
                        hint_text="0.00",
                        keyboard_type=ft.KeyboardType.NUMBER,
                        input_filter=ft.InputFilter(
                            regex_string=r"^\d*\.?\d*$", allow=True
                        ),
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
            )
        ]
