import flet as ft

from src.components.budget_edit import BudgetEdit


@ft.component
def App():
    return ft.Router([
        ft.Route(path="budgets/:budget_id/edit", component=BudgetEdit),
    ])

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))
