import reflex as rx
from .components.card import card_component
from .components.experience_card import card_xp


from rxconfig import config


def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.flex(
                rx.avatar(
                    src="/profile.jpg",
                    class_name="size-72 rounded-full shadow-lg mr-12"
                ),
                rx.vstack(
                    rx.heading(
                        "Rafael Eduardo Rosales Rivas",
                        size="4",
                    ),
                    rx.flex(
                        rx.heading(
                            "Full-Stack Developer",
                            size="9",
                            class_name="text-yellow-500"   
                        ),
                        rx.heading(
                            "Backend Specialist",
                            size="9",   
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text("Construyo sistemas empresariales escalables y APIs robustas.",),
                        rx.text("Especializado en soluciones para el sector salud y sistemas de alta seguridad."),
                        direction="column",
                        spacing="1",
                        
                    ),
                    rx.flex(
                        rx.button(
                        rx.icon(tag="folder-down", class_name="mr-2"),
                        "Descargar CV",
                        on_click=rx.download(url="/CV-Rafael-Eduardo-Rosales-Rivas-2025.pdf"),
                        class_name="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",
                        ),
                        rx.link(
                            rx.button(
                                rx.icon(tag="linkedin", class_name="mr-2"),
                                "LinkedIn",
                                class_name="bg-gray-800 hover:bg-gray-900 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",),
                            href="https://www.linkedin.com/in/rafael-rosales-dev/",
                            
                        ),
                        rx.link(
                            rx.button(
                            rx.icon(tag="github", class_name="mr-2"),
                            "GitHub",
                            class_name="bg-gray-800 hover:bg-gray-900 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",
                            ml="4",),
                            href="https://github.com/rafpsyDev",
                        ),
                        spacing="2",
                    ),
                ),
            ),
            class_name="w-full h-[75vh] flex items-center justify-center"
        ),
        #SECCION SOBRE MI#
        rx.box(
            rx.blockquote("Sobre mí", size="7", class_name="mb-8 mt-12", color_scheme="yellow"),
            rx.flex(
                rx.box(
                    rx.text(
                    "Ingeniero de software ", rx.text.strong("con 3+ años de experiencia formal", class_name="text-yellow-500"), " y experiencia adicional durante mis estudios universitarios. Mi trayectoria profesional se ha centrado en el desarrollo de sistemas empresariales complejos.",
                    class_name="mb-12 mt-8",
                    ),
                    rx.text(
                        "Aunque mi pasión está en el",rx.text.strong(" frontend", class_name="text-yellow-500"), " he desarrollado la mayor parte de mi carrera en ",rx.text.strong("backend", class_name="text-yellow-500"), ", creando APIs escalables y sistemas a medida principalmente para el sector salud."
                    ),
                    class_name="w-2/3 mr-8"
                ),
                rx.box(
                    card_component(),
                )
            ),
            class_name="w-full h-[70vh] "
        ),
        #SECCION EXPERIENCIA#
        rx.box(
            rx.blockquote("Experiencia", size="7", class_name="mb-8 mt-12", color_scheme="yellow"),
            rx.vstack(
                card_xp(),
                card_xp(),
                class_name="w-full space-y-4 gap-4"
            ),
            class_name="w-full "
        ),
        #SECCION EXPERIENCIA#
        rx.box(
            rx.blockquote("Proyectos destacados", size="7", class_name="mb-8 mt-12", color_scheme="yellow"),
            class_name="w-full h-[70vh] "
        ),
        #Habilidades técnicas#
        rx.box(
            rx.blockquote("Habilidades técnicas", size="7", class_name="mb-8 mt-12", color_scheme="yellow"),
            class_name="w-full h-[70vh] "
        ),
        #Contacto#
        rx.box(
            rx.blockquote("Contacto", size="7", class_name="mb-8 mt-12", color_scheme="yellow"),
            class_name="w-full h-[70vh] "
        ),
    )


app = rx.App()
app.add_page(index)
