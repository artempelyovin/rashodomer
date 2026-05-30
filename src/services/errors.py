class BaseServiceError(Exception):
    pass


class BudgetNotFound(BaseServiceError):
    def __init__(self, budget_id: str):
        self.budget_id = budget_id
        super().__init__(f"Budget with id {budget_id} not found")


class CategoryNotFound(BaseServiceError):
    def __init__(self, category_id: str):
        self.category_id = category_id
        super().__init__(f"Category with id {category_id} not found")
