import flet as ft
from flet import Control

from services.errors import BudgetNotFound
from src.components.budget_edit import BudgetEdit
from src.services.budget import FileBudgetService
from ui_utils import show_error


@ft.component
def BudgetPage() -> Control:
    params = ft.use_route_params()
    budget_id = params["budget_id"]
    budget_service = FileBudgetService()  # TODO: не юзать напрямую реализацию!
    try:
        budget = budget_service.get(budget_id)
    except BudgetNotFound:
        show_error("Budget not found")
        return ft.context.page.navigate("/budgets")
    return BudgetEdit(budget=budget)
