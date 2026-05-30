class BaseServiceError(Exception):
    pass


class BudgetNotFound(BaseServiceError):
    pass


class CategoryNotFound(BaseServiceError):
    pass
