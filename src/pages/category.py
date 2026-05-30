import flet as ft

from components.category_create import CategoryCreate
from components.category_detail import CategoryDetail
from components.category_edit import CategoryEdit
from components.category_list import CategoryList
from context import CategoryServiceProvider
from models import CategoryType
from services.errors import CategoryNotFound
from ui_utils import navigate, show_error


@ft.component
def CategoryListPage() -> ft.Control:
    category_service = ft.use_context(CategoryServiceProvider)

    category_type, set_category_type = ft.use_state(None)
    only_active, set_only_active = ft.use_state(False)

    categories = category_service.list(category_type=category_type, only_active=only_active)

    return CategoryList(
        categories=categories,
        category_type=category_type,
        only_active=only_active,
        on_type_change=set_category_type,
        on_filter_change=set_only_active,
        on_category_click=lambda category_id: navigate(f"/categories/{category_id}"),
        on_add_button_click=lambda _: navigate("/categories/new"),
    )


@ft.component
def CategoryCreatePage() -> ft.Control:
    category_service = ft.use_context(CategoryServiceProvider)

    def on_save(name: str, description: str, category_type: CategoryType) -> None:
        category_service.create(name=name, description=description, category_type=category_type)
        navigate("/categories")

    return CategoryCreate(
        on_cancel=lambda _: navigate("/categories"),
        on_save=on_save,
    )


@ft.component
def CategoryPage() -> ft.Control:
    params = ft.use_route_params()
    category_id = params["category_id"]
    category_service = ft.use_context(CategoryServiceProvider)

    is_editing, set_is_editing = ft.use_state(False)

    try:
        category = category_service.get(category_id)
    except CategoryNotFound as e:
        show_error(str(e))
        return navigate("/categories")

    def on_save(category_id: str, name: str, description: str, category_type: CategoryType, is_active: bool) -> None:
        category_service.update(
            category_id=category_id,
            name=name,
            description=description,
            category_type=category_type,
            is_active=is_active,
        )
        navigate("/categories")

    def on_delete() -> None:
        category_service.delete(category_id=category_id)
        navigate("/categories")

    if is_editing:
        return CategoryEdit(
            category=category,
            on_cancel=lambda _: set_is_editing(False),
            on_save=on_save,
        )
    else:
        return CategoryDetail(
            category=category,
            on_cancel=lambda _: navigate("/categories"),
            on_edit=lambda _: set_is_editing(True),
            on_delete=on_delete,
        )
