import reflex as rx

def hero_section() -> rx.Component:
    return rx.box(
        rx.avatar(
            src="/profile.jpg",
            class_name=" size-72 rounded-full shadow-lg mr-12 hidden md:block"
        ),
        rx.vstack(
            rx.heading(
                "Rafael Eduardo Rosales Rivas",
                font_family="GeistMono",
                class_name="text-md font-stretch-ultra-condensed -mb-3",
            ),
            rx.flex(
                rx.heading(
                    "Full-Stack Developer",
                    font_family="Gotham_Black",
                    class_name=" text-4xl lg:text-5xl tracking-tight text-start text-yellow-500"   
                ),
                rx.heading(
                    "Backend Specialist",
                    font_family="Gotham_Black",
                    class_name=" text-4xl lg:text-5xl tracking-tight text-start",   
                ),
                direction="column",
                spacing="1",
            ),
            rx.flex(
                rx.text("Construyo sistemas empresariales escalables y APIs robustas.",),
                rx.text("Especializado en soluciones para el sector salud y sistemas de alta seguridad."),
                direction="column",
                font_family="Montserrat",
                spacing="1",
                class_name="text-base",
            ),
            rx.flex(
                rx.button(
                rx.icon(tag="folder-down", class_name="mr-2"),
                "Descargar CV",
                font_family="Montserrat",
                on_click=rx.download(url="/CV-Rafael-Eduardo-Rosales-Rivas-2025.pdf"),
                class_name="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",
                ),
                rx.link(
                    rx.button(
                        rx.icon(tag="linkedin", class_name="mr-2"),
                        "LinkedIn",
                        font_family="Montserrat",
                        class_name="bg-gray-800 hover:bg-gray-900 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",),
                    href="https://www.linkedin.com/in/rafael-rosales-dev/",
                    
                ),
                rx.link(
                    rx.button(
                    rx.icon(tag="github", class_name="mr-2"),
                    "GitHub",
                    font_family="Montserrat",
                    class_name="bg-gray-800 hover:bg-gray-900 text-white font-semibold py-2 px-6 rounded-full shadow-md transition-all duration-300",
                    ml="4",),
                    href="https://github.com/rafpsyDev",
                ),
                spacing="2",
            ),
        ),
    class_name="w-full md:h-[75vh] flex items-center justify-center mt-12 md:mt-0"
    )