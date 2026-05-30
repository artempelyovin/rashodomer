import flet as ft

from services.file import FileBudgetService, FileCategoryService

BudgetServiceProvider = ft.create_context(FileBudgetService())
CategoryServiceProvider = ft.create_context(FileCategoryService())
