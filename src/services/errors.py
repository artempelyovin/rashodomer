class BaseServiceError(Exception):
    pass


class BudgetNotFound(BaseServiceError):
    pass
