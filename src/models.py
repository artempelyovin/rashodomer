from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

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
