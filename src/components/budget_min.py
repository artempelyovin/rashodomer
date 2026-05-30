from decimal import Decimal
from typing import Callable

import flet as ft

from models import BudgetModel


@ft.component
def BudgetMin(budget: BudgetModel, on_click: Callable) -> ft.Control:
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
