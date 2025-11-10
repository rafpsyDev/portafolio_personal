import reflex as rx

from .partials.hero import hero_section
from .partials.experiencia import experiencia_section
from .partials.seccion_skills import seccion_skills
from .partials.contact_section import contact_section
from .partials.about import about_section
from .partials.proyect_section import ProjectSection


def index() -> rx.Component:
    return rx.container(
        hero_section(),
        about_section(),
        experiencia_section(),
        #SECCION EXPERIENCIA#
        ProjectSection(),
        #Habilidades técnicas#
        seccion_skills(),
        #Contacto#
        contact_section(),
    )


app = rx.App(
    stylesheets=["/styles.css"],
)
app.add_page(index)
