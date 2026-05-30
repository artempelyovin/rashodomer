from typing import Callable

import flet as ft

from models import CategoryModel, CategoryType


@ft.component
def CategoryMin(category: CategoryModel, on_click: Callable) -> ft.Control:
    icon = ft.Icons.ARROW_UPWARD if category.type == CategoryType.INCOME else ft.Icons.ARROW_DOWNWARD
    color = ft.Colors.GREEN if category.type == CategoryType.INCOME else ft.Colors.RED

    return ft.Container(
        ft.Row(
            [
                ft.Icon(icon, color=color),
                ft.Column(
                    [
                        ft.Text(category.name, weight=ft.FontWeight.BOLD),
                        ft.Text(category.description or category.type.value, color=ft.Colors.SECONDARY),
                    ],
                    spacing=0,
                ),
            ]
        ),
        padding=10,
        border_radius=ft.BorderRadius.all(10),
        ink=True,
        on_click=on_click,
    )


@ft.component
def CategoryList(
    categories: list[CategoryModel],
    category_type: CategoryType | None,
    only_active: bool,
    on_type_change: Callable,
    on_filter_change: Callable,
    on_category_click: Callable,
    on_add_button_click: Callable,
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
                        content="Все",
                        style=tab_style(category_type is None),
                        on_click=lambda _: on_type_change(None),
                    ),
                    ft.TextButton(
                        content="Доходы",
                        style=tab_style(category_type == CategoryType.INCOME),
                        on_click=lambda _: on_type_change(CategoryType.INCOME),
                    ),
                    ft.TextButton(
                        content="Расходы",
                        style=tab_style(category_type == CategoryType.EXPENSE),
                        on_click=lambda _: on_type_change(CategoryType.EXPENSE),
                    ),
                    ft.TextButton(
                        content="Активные",
                        style=tab_style(only_active),
                        on_click=lambda _: on_filter_change(not only_active),
                    ),
                ]
            ),
            ft.Column(
                [
                    CategoryMin(
                        category=category,
                        on_click=lambda _, c=category: on_category_click(c.id),
                    )
                    for category in categories
                ]
            ),
            ft.Row(
                [
                    ft.Container(expand=True),
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=on_add_button_click),
                ],
            ),
        ]
    )
