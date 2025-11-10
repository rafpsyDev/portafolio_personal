import reflex as rx
from ..components.project_card import project_card
from ..data.projects_data import projects

def ProjectSection() -> rx.Component:
    return rx.box(
        rx.blockquote(
            "Proyectos destacados",
            size="7",
            class_name="mb-8 mt-8",
            font_family="Gotham-Black",
            color_scheme="yellow"
        ),
        rx.box(
            *[project_card(**project) for project in projects], 
            class_name="grid grid-cols-1 md:grid-cols-2 gap-4"
        ),
        class_name="w-full py-8"
    )