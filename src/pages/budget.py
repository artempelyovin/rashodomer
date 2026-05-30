from decimal import Decimal

import flet as ft

from components.budget_create import BudgetCreate
from components.budget_detail import BudgetDetail
from components.budget_edit import BudgetEdit
from components.budget_list import BudgetList
from context import BudgetServiceProvider
from services.errors import BudgetNotFound
from ui_utils import show_error


@ft.component
def BudgetListPage() -> ft.Control:
    budget_service = ft.use_context(BudgetServiceProvider)

    only_active, set_only_active = ft.use_state(True)
    budgets = budget_service.list(only_active=only_active)
    return BudgetList(
        budgets=budgets,
        only_active=only_active,
        on_filter_change=set_only_active,
        on_budget_click=lambda budget_id: ft.context.page.navigate(f"/budgets/{budget_id}"),
        on_add_button_click=lambda _: ft.context.page.navigate(f"/budgets/new"),
    )


@ft.component
def BudgetCreatePage() -> ft.Control:
    budget_service = ft.use_context(BudgetServiceProvider)

    def on_save(name: str, description: str, amount: str) -> None:
        budget_service.create(name=name, description=description, amount=Decimal(amount))
        ft.context.page.navigate("/budgets")

    return BudgetCreate(
        on_cancel=lambda budget_id: ft.context.page.navigate(f"/budgets"),
        on_save=on_save,
    )


@ft.component
def BudgetPage() -> ft.Control:
    params = ft.use_route_params()
    budget_id = params["budget_id"]
    budget_service = ft.use_context(BudgetServiceProvider)

    def on_save(budget_id: str, name: str, description: str, amount: str, is_active: bool) -> None:
        budget_service.update(
            budget_id=budget_id, name=name, description=description, amount=Decimal(amount), is_active=is_active
        )
        ft.context.page.navigate("/budgets")

    def on_delete() -> None:
        budget_service.delete(budget_id=budget_id)
        ft.context.page.navigate("/budgets")

    is_editing, set_is_editing = ft.use_state(False)
    try:
        budget = budget_service.get(budget_id)
    except BudgetNotFound as e:
        show_error(str(e))
        return ft.context.page.navigate("/budgets")
    if is_editing:
        return BudgetEdit(budget=budget, on_cancel=lambda _: set_is_editing(False), on_save=on_save)
    else:
        return BudgetDetail(
            budget=budget,
            on_cancel=lambda _: ft.context.page.navigate("/budgets"),
            on_edit=lambda _: set_is_editing(True),
            on_delete=on_delete,
        )
