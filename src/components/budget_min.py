from typing import Callable

import flet as ft

from models import BudgetModel


@ft.component
def BudgetMin(budget: BudgetModel, on_click: Callable) -> ft.Control:
    if budget.amount >= 0:
        amount_color = ft.Colors.GREEN
        amount_sign = "+"
    else:
        amount_color = ft.Colors.RED
        amount_sign = "-"
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
                ft.Text(f"{amount_sign}{budget.amount}₽", color=amount_color, size=20),
            ]
        ),
        padding=10,
        border_radius=ft.BorderRadius.all(10),
        ink=True,
        on_click=on_click,
    )
