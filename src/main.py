import flet as ft

from pages.budget import BudgetCreate, BudgetListPage, BudgetPage


@ft.component
def App():
    return ft.Router(
        [
            ft.Route(path="budgets", component=BudgetListPage),
            ft.Route(path="budgets/new", component=BudgetCreate),
            ft.Route(path="budgets/:budget_id", component=BudgetPage),
        ]
    )


if __name__ == "__main__":
    ft.run(lambda page: page.render(App), host="0.0.0.0", port=60000)
