from abc import ABC, abstractmethod
from decimal import Decimal

from models import BudgetModel, CategoryModel, CategoryType


class BudgetService(ABC):
    @abstractmethod
    def create(self, name: str, description: str, amount: Decimal) -> BudgetModel: ...

    @abstractmethod
    def get(self, budget_id: str) -> BudgetModel: ...

    @abstractmethod
    def list(self, only_active: bool = False) -> list[BudgetModel]: ...

    @abstractmethod
    def update(
        self,
        budget_id: str,
        name: str,
        description: str,
        amount: Decimal,
        is_active: bool,
    ) -> BudgetModel: ...

    @abstractmethod
    def delete(self, budget_id: str) -> None: ...


class CategoryService(ABC):
    @abstractmethod
    def create(self, name: str, category_type: CategoryType, description: str = "") -> CategoryModel: ...

    @abstractmethod
    def get(self, category_id: str) -> CategoryModel: ...

    @abstractmethod
    def list(self, category_type: CategoryType | None = None, only_active: bool = False) -> list[CategoryModel]: ...

    @abstractmethod
    def update(
        self,
        category_id: str,
        name: str,
        category_type: CategoryType,
        description: str,
        is_active: bool,
    ) -> CategoryModel: ...

    @abstractmethod
    def delete(self, category_id: str) -> None: ...
