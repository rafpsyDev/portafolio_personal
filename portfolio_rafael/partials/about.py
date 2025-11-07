import reflex as rx
from ..components.about_card import about_me_card

def about_section() -> rx.Component:
    return rx.box(
        rx.blockquote("Sobre mí", size="7", class_name="mt-8", font_family="Gotham-Black", color_scheme="yellow"),
        rx.flex(
            rx.box(
                rx.text(
                "Ingeniero de software ", rx.text.strong("con 3+ años de experiencia formal", class_name="text-yellow-500"), " y experiencia adicional durante mis estudios universitarios. Mi trayectoria profesional se ha centrado en el desarrollo de sistemas empresariales complejos.",
                class_name="mb-12 mt-8",
                font_family="Montserrat",
                ),
                rx.text(
                    "Aunque mi pasión está en el",rx.text.strong(" frontend", class_name="text-yellow-500"), " he desarrollado la mayor parte de mi carrera en ",rx.text.strong("backend", class_name="text-yellow-500"), ", creando APIs escalables y sistemas a medida principalmente para el sector salud.",
                    font_family="Montserrat",
                ),
                class_name=" md:w-2/3 mr-8 mb-12 md:mb-0 text-base",
                ),
                rx.box(
                    about_me_card(),
                ),
                class_name="flex flex-col md:flex-row justify-between items-center md:items-center md:gap-8"
            ),
        class_name="w-full md:mt-20" 
        ),
