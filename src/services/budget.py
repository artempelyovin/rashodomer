import json
import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal

from services.errors import BudgetNotFound
from src.models import BudgetModel


class BudgetService(ABC):
    @abstractmethod
    def create(self, name: str, description: str, amount: Decimal) -> BudgetModel: ...

    @abstractmethod
    def get(self, budget_id: str) -> BudgetModel: ...

    @abstractmethod
    def list(self) -> list[BudgetModel]: ...

    @abstractmethod
    def update(self, budget_id: str, name: str, description: str, amount: Decimal, is_active: bool) -> BudgetModel: ...

    @abstractmethod
    def delete(self, budget_id: int) -> BudgetModel: ...


class FileBudgetService(BudgetService):

    def __init__(self):
        self.file_path = "budgets.json"
        self._init_storage()

    def _init_storage(self) -> None:
        if not os.path.exists(self.file_path):
            self._save([])

    def _load(self) -> list[dict]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self, data: list[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def _serialize_model(model: BudgetModel) -> dict:
        return {
            "id": model.id,
            "name": model.name,
            "description": model.description,
            "amount": str(model.amount),  # Decimal -> str
            "is_active": model.is_active,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
        }

    @staticmethod
    def _deserialize_model(data: dict) -> BudgetModel:
        """Создаёт BudgetModel из словаря, загруженного из JSON."""
        return BudgetModel(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            amount=Decimal(data["amount"]),  # str -> Decimal
            is_active=data["is_active"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    def create(self, name: str, description: str, amount: Decimal) -> BudgetModel:
        existing_models = self.list()
        now = datetime.now()

        new_model = BudgetModel(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            amount=amount,
            is_active=True,
            created_at=now,
            updated_at=now,
        )

        all_models = existing_models + [new_model]
        self._save([self._serialize_model(m) for m in all_models])
        return new_model

    def get(self, budget_id: str) -> BudgetModel:
        models = self.list()
        for model in models:
            if model.id == budget_id:
                return model
        raise BudgetNotFound(f"Budget with id {budget_id} not found")

    def list(self) -> list[BudgetModel]:
        raw_data = self._load()
        return [self._deserialize_model(item) for item in raw_data]

    def update(self, budget_id: str, name: str, description: str, amount: Decimal, is_active: bool) -> BudgetModel:
        models = self.list()
        updated_model = None
        for i, model in enumerate(models):
            if model.id == budget_id:
                updated_model = BudgetModel(
                    id=model.id,
                    name=name,
                    description=description,
                    amount=amount,
                    is_active=is_active,
                    created_at=model.created_at,
                    updated_at=datetime.now(),
                )
                models[i] = updated_model
                break
        if updated_model is None:
            raise BudgetNotFound(f"Budget with id {budget_id} not found")
        self._save([self._serialize_model(m) for m in models])
        return updated_model

    def delete(self, budget_id: int) -> BudgetModel:
        str_id = str(budget_id)
        models = self.list()
        for i, model in enumerate(models):
            if model.id == str_id:
                removed = models.pop(i)
                self._save([self._serialize_model(m) for m in models])
                return removed
        raise BudgetNotFound(f"Budget with id {budget_id} not found")
