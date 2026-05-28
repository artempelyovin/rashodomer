import flet as ft

from components.budget_edit import BudgetEdit
from services.errors import BudgetNotFound
from src.components.budget_detail import BudgetDetail
from src.services.budget import FileBudgetService
from ui_utils import show_error


@ft.component
def BudgetPage() -> ft.Control:
    params = ft.use_route_params()
    budget_id = params["budget_id"]
    budget_service = FileBudgetService()  # TODO: не юзать напрямую реализацию!

    is_editing, set_is_editing = ft.use_state(False)
    try:
        budget = budget_service.get(budget_id)
    except BudgetNotFound:
        show_error("Budget not found")
        return ft.context.page.navigate("/budgets")
    if is_editing:
        return BudgetEdit(budget=budget, on_cancel=lambda _: set_is_editing(False))
    else:
        return BudgetDetail(budget=budget, on_edit=lambda _: set_is_editing(True))
