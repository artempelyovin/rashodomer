from typing import Callable

import flet as ft

from components.budget_min import BudgetMin
from models import BudgetModel


@ft.component
def BudgetList(budgets: list[BudgetModel], on_budget_click: Callable, on_add_button_click: Callable) -> ft.Control:
    return ft.Column(
        [
            ft.Column([BudgetMin(budget=budget, on_click=lambda _: on_budget_click(budget.id)) for budget in budgets]),
            ft.Row(
                [
                    ft.Container(expand=True),
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=on_add_button_click),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
        ]
    )
