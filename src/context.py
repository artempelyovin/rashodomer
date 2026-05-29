import flet as ft

from services.budget import FileBudgetService

BudgetServiceProvider = ft.create_context(FileBudgetService())
