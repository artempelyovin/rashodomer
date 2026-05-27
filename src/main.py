from datetime import datetime
from decimal import Decimal

import flet as ft
from flet import TemplateRoute

from src.models import BudgetModel
from src.views.budget_edit import BudgetEditView


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

    def route_change(e: ft.RouteChangeEvent):
        template_route = TemplateRoute(page.route)
        if template_route.match("/budgets/:budget_id/edit"):
            budget_id = template_route.budget_id
            page.views.append(BudgetEditView(budget=budget))
        page.update()

    page.on_route_change = route_change


ft.app(target=main)
