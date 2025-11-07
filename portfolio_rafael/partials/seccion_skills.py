import reflex as rx

from ..data.skills import skills
from ..components.skill_card import card_skill

def seccion_skills() -> rx.Component:
    return rx.box(
        rx.blockquote(
            "Habilidades técnicas",
            size="7",
            class_name="mb-8 mt-8",
            font_family="Gotham-Black",
            color_scheme="yellow"
        ),
        rx.box(
            rx.text(
                "Stack tecnológico y competencias desarrolladas a lo largo de mi carrera profesional.",
                font_family="Montserrat",
            ),
            rx.box(
                *[card_skill(**pack) for pack in skills],
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8",
            ),
            rx.vstack(
                rx.heading(
                    "Actualmente aprendiendo",
                    size="4",
                    font_family="Montserrat",
                    class_name="font-bold"
                ),
                rx.text(
                    "Estoy expandiendo mis habilidades en el ecosistema de JavaScript moderno, enfocándome en",rx.text.strong(" Node.js",class_name="text-yellow-500")," y ",rx.text.strong("Next.js",class_name="text-yellow-500")," para fortalecer mi perfil full-stack y poder liderar proyectos con tecnologías de última generación.",
                    font_family="Montserrat",
                    class_name="mt-4 text-base"
                ),
                rx.flex(
                    rx.badge("Node.js", color_scheme="yellow", size="2", font_family="GeistMono"),
                    rx.badge("Next.js", color_scheme="yellow", size="2", font_family="GeistMono"),
                    rx.badge("TypeScript", color_scheme="yellow", size="2", font_family="GeistMono"),
                    class_name="mt-4 flex-wrap gap-2",
                ),
                class_name="border border-solid border-yellow-300 shadow-xl  rounded-2xl p-6 m-2 w-full",
            ),
            
        ),
        class_name="w-full"
    )