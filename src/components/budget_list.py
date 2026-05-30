from typing import Any, Callable

import flet as ft

from components.budget_min import BudgetMin
from models import BudgetModel


@ft.component
def BudgetList(
    budgets: list[BudgetModel],
    only_active: bool,
    on_filter_change: Any,
    on_budget_click: Callable,
    on_add_button_click: Callable,
) -> ft.Control:
    return ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        content="Активные",
                        style=ft.ButtonStyle(
                            color=ft.Colors.PRIMARY if only_active else ft.Colors.SECONDARY,
                            bgcolor=ft.Colors.SECONDARY_CONTAINER if only_active else ft.Colors.TRANSPARENT,
                            shape=ft.StadiumBorder(),
                        ),
                        on_click=lambda _: on_filter_change(True),
                    ),
                    ft.TextButton(
                        content="Все",
                        style=ft.ButtonStyle(
                            color=ft.Colors.PRIMARY if not only_active else ft.Colors.SECONDARY,
                            bgcolor=ft.Colors.SECONDARY_CONTAINER if not only_active else ft.Colors.TRANSPARENT,
                            shape=ft.StadiumBorder(),
                        ),
                        on_click=lambda _: on_filter_change(False),
                    ),
                ]
            ),
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
