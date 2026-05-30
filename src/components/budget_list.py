from decimal import Decimal
from typing import Callable

import flet as ft

from models import BudgetModel


@ft.component
def BudgetListItem(budget: BudgetModel, on_click: Callable) -> ft.Control:
    if budget.amount == Decimal(0):
        amount_color = ft.Colors.GREY
        amount_str = f"{budget.amount}₽"
    elif budget.amount > Decimal(0):
        amount_color = ft.Colors.GREEN
        amount_str = f"+{budget.amount}₽"
    else:
        amount_color = ft.Colors.RED
        amount_str = f"{budget.amount}₽"  # минус уже есть в числе
    return ft.Container(
        ft.Row(
            [
                ft.Icon(ft.Icons.MONEY),
                ft.Column(
                    [
                        ft.Text(budget.name, weight=ft.FontWeight.BOLD),
                        ft.Text(budget.description),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text(amount_str, color=amount_color, size=20),
            ]
        ),
        padding=10,
        border_radius=ft.BorderRadius.all(10),
        ink=True,
        on_click=on_click,
    )


@ft.component
def BudgetList(
    budgets: list[BudgetModel],
    only_active: bool,
    on_filter_change: Callable,
    on_budget_click: Callable,
    on_add_click: Callable,
) -> ft.Control:
    def tab_style(active: bool) -> ft.ButtonStyle:
        return ft.ButtonStyle(
            color=ft.Colors.PRIMARY if active else ft.Colors.SECONDARY,
            bgcolor=ft.Colors.SECONDARY_CONTAINER if active else ft.Colors.TRANSPARENT,
            shape=ft.StadiumBorder(),
        )

    return ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        content="Активные",
                        style=tab_style(only_active),
                        on_click=lambda _: on_filter_change(True),
                    ),
                    ft.TextButton(
                        content="Все",
                        style=tab_style(not only_active),
                        on_click=lambda _: on_filter_change(False),
                    ),
                ]
            ),
            ft.Column(
                [BudgetListItem(budget=budget, on_click=lambda _: on_budget_click(budget.id)) for budget in budgets]
            ),
            ft.Row(
                [
                    ft.Container(expand=True),
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=on_add_click),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
        ]
    )
