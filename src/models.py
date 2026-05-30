from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import StrEnum

import flet as ft


@ft.observable
@dataclass
class BudgetModel:
    id: str
    name: str
    description: str
    amount: Decimal
    is_active: bool
    created_at: datetime
    updated_at: datetime


class CategoryType(StrEnum):
    INCOME = "income"
    EXPENSE = "expense"


@ft.observable
@dataclass
class CategoryModel:
    id: str
    name: str
    type: CategoryType
    is_active: bool
    created_at: datetime
    updated_at: datetime
    description: str = ""
