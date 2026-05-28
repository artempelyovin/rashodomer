import flet as ft
from flet import Control

from src.components.budget_edit import BudgetEdit
from src.services.budget import FileBudgetService


@ft.component
def BudgetPage() -> Control:
    params = ft.use_route_params()
    budget_id = params["budget_id"]
    budget_service = FileBudgetService()  # TODO: не юзать напрямую реализацию!
    budget = budget_service.get(budget_id)
    return BudgetEdit(budget=budget)
