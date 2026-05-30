import flet as ft

from pages.budget import BudgetCreatePage, BudgetListPage, BudgetPage
from pages.category import CategoryCreatePage, CategoryListPage, CategoryPage


@ft.component
def App():
    return ft.Router(
        [
            ft.Route(path="/budgets", component=BudgetListPage),
            ft.Route(path="/budgets/new", component=BudgetCreatePage),
            ft.Route(path="/budgets/:budget_id", component=BudgetPage),
            ft.Route(path="/categories", component=CategoryListPage),
            ft.Route(path="/categories/new", component=CategoryCreatePage),
            ft.Route(path="/categories/:category_id", component=CategoryPage),
        ]
    )


if __name__ == "__main__":
    ft.run(lambda page: page.render(App), host="0.0.0.0", port=60000)
