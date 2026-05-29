import flet as ft

from components.budget_edit import BudgetEdit
from components.budget_list import BudgetList
from services.errors import BudgetNotFound
from src.components.budget_detail import BudgetDetail
from src.services.budget import FileBudgetService
from ui_utils import show_error


@ft.component
def BudgetListPage() -> ft.Control:
    budget_service = FileBudgetService()  # TODO: не юзать напрямую реализацию!
    budgets = budget_service.list()
    return BudgetList(
        budgets=budgets,
        on_budget_click=lambda budget_id: ft.context.page.navigate(f"/budgets/{budget_id}"),
        on_add_button_click=lambda _: ft.context.page.navigate(f"/budgets/new"),
    )


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
        return BudgetDetail(
            budget=budget,
            on_cancel=lambda _: ft.context.page.navigate("/budgets"),
            on_edit=lambda _: set_is_editing(True),
        )
