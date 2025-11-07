import reflex as rx

def about_me_card():
    return rx.card(
        rx.vstack(
            rx.text.strong(
                "Experiencia destacada",
                font_family="GeistMono",
                class_name="text-xl"
            ),
            rx.hstack(
                rx.unordered_list(
                    rx.list_item("Liderazgo de proyectos end-to-end: desde cliente hasta arquitectura técnica"),
                    rx.list_item("Sistemas para hospitales medianos con alto nivel de complejidad"),
                    rx.list_item("Sistemas de almacén con seguridad avanzada y biometría"),
                    rx.list_item("Integración con servicios de terceros y APIs."),
                    rx.list_item("Cumplimiento normativo (SAT) y validación de lotes"),
                    font_family="Montserrat",
                    class_name="list-disc pl-5 space-y-2 text-base",
                ),
            ),
        ),
        variant="surface",
        class_name="border border-solid border-yellow-300 rounded-2xl p-6 m-2 shadow-lg"
    )
