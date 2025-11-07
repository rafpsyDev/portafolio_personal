import reflex as rx

from .partials.hero import hero_section
from .partials.experiencia import experiencia_section
from .partials.seccion_skills import seccion_skills
from .partials.contact_section import contact_section
from .partials.about import about_section



def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        hero_section(),
        about_section(),
        experiencia_section(),
        #SECCION EXPERIENCIA#
        rx.box(
            rx.blockquote(
                "Proyectos destacados",
                size="7",
                class_name="mb-8 mt-8",
                font_family="Gotham-Black",
                color_scheme="yellow"
            ),
            class_name="w-full h-[70vh] "
        ),
        #Habilidades técnicas#
        seccion_skills(),
        #Contacto#
        contact_section(),
    )


app = rx.App(
    stylesheets=["/styles.css"],
)
app.add_page(index)
