import json
import os
import uuid
from datetime import datetime
from decimal import Decimal

from models import BudgetModel, CategoryModel, CategoryType
from services.abc import BudgetService, CategoryService
from services.errors import BudgetNotFound, CategoryNotFound


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
        raise BudgetNotFound(budget_id)

    def list(self, only_active: bool = False) -> list[BudgetModel]:
        raw_data = self._load()
        models = [self._deserialize_model(item) for item in raw_data]
        if only_active:
            models = [model for model in models if model.is_active]
        return models

    def update(
        self,
        budget_id: str,
        name: str,
        description: str,
        amount: Decimal,
        is_active: bool,
    ) -> BudgetModel:
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
            raise BudgetNotFound(budget_id)
        self._save([self._serialize_model(m) for m in models])
        return updated_model

    def delete(self, budget_id: str) -> BudgetModel:
        models = self.list()
        for i, model in enumerate(models):
            if model.id == budget_id:
                removed = models.pop(i)
                self._save([self._serialize_model(m) for m in models])
                return removed
        raise BudgetNotFound(budget_id)

class FileCategoryService(CategoryService):
    def __init__(self):
        self.file_path = "categories.json"
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
    def _serialize_model(model: CategoryModel) -> dict:
        return {
            "id": model.id,
            "name": model.name,
            "type": model.type.value,
            "description": model.description,
            "is_active": model.is_active,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
        }

    @staticmethod
    def _deserialize_model(data: dict) -> CategoryModel:
        return CategoryModel(
            id=data["id"],
            name=data["name"],
            type=CategoryType(data["type"]),
            description=data["description"],
            is_active=data["is_active"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    def create(self, name: str, category_type: CategoryType, description: str = "") -> CategoryModel:
        now = datetime.now()
        new_model = CategoryModel(
            id=str(uuid.uuid4()),
            name=name,
            type=category_type,
            description=description,
            is_active=True,
            created_at=now,
            updated_at=now,
        )
        existing = self.list()
        self._save([self._serialize_model(m) for m in existing + [new_model]])
        return new_model

    def get(self, category_id: str) -> CategoryModel:
        for model in self.list():
            if model.id == category_id:
                return model
        raise CategoryNotFound(category_id)

    def list(
        self,
        category_type: CategoryType | None = None,
        only_active: bool = False,
    ) -> list[CategoryModel]:
        models = [self._deserialize_model(item) for item in self._load()]
        if category_type is not None:
            models = [m for m in models if m.type == category_type]
        if only_active:
            models = [m for m in models if m.is_active]
        return models

    def update(
        self,
        category_id: str,
        name: str,
        category_type: CategoryType,
        description: str,
        is_active: bool,
    ) -> CategoryModel:
        models = self.list()
        updated_model = None
        for i, model in enumerate(models):
            if model.id == category_id:
                updated_model = CategoryModel(
                    id=model.id,
                    name=name,
                    type=category_type,
                    description=description,
                    is_active=is_active,
                    created_at=model.created_at,
                    updated_at=datetime.now(),
                )
                models[i] = updated_model
                break
        if updated_model is None:
            raise CategoryNotFound(category_id)
        self._save([self._serialize_model(m) for m in models])
        return updated_model

    def delete(self, category_id: str) -> None:
        models = self.list()
        for i, model in enumerate(models):
            if model.id == category_id:
                models.pop(i)
                self._save([self._serialize_model(m) for m in models])
                return
        raise CategoryNotFound(category_id)
