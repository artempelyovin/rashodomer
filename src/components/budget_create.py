from typing import Callable

import flet as ft


@ft.component
def BudgetCreate(on_cancel: Callable, on_save: Callable) -> ft.Control:
    name, set_name = ft.use_state("")
    description, set_description = ft.use_state("")
    amount, set_amount = ft.use_state("")

    def handle_save():
        on_save(name=name, description=description, amount=amount)

    return ft.Column(
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_cancel),
                    ft.Text("Создание бюджета", size=24),
                    ft.IconButton(icon=ft.Icons.CHECK, on_click=handle_save),
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
                label="Сумма",
                value=amount,
                on_change=lambda e: set_amount(e.control.value),
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$", allow=True),
                text_align=ft.TextAlign.RIGHT,
            ),
        ]
    )
