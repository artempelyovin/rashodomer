from typing import Callable

import flet as ft

from src.models import BudgetModel
from src.utils import format_datetime


@ft.component
def BudgetDetail(budget: BudgetModel, on_cancel: Callable, on_edit: Callable) -> ft.Control:
    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Обзор бюджета", size=24),
                ]
            ),
            ft.Row(
                [
                    ft.Text("ID:"),
                    ft.Text(budget.id),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Название:"),
                    ft.Text(budget.name),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Описание:"),
                    ft.Text(budget.description),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Сумма:"),
                    ft.Text(str(budget.amount)),
                ]
            ),
            ft.Switch(label="Архивирован", value=budget.is_active, disabled=True),
            ft.Row(
                [
                    ft.Text("Создано:"),
                    ft.Text(value=format_datetime(budget.created_at)),
                ]
            ),
            ft.Row(
                [
                    ft.Text("Обновлено:"),
                    ft.Text(value=format_datetime(budget.updated_at)),
                ]
            ),
            ft.FloatingActionButton(icon=ft.Icons.EDIT, on_click=on_edit),
        ]
    )
