import reflex as rx

def card_component():
    return rx.box(
        rx.vstack(
            rx.text.strong(
                "Experiencia destacada",
                class_name="text-xl"
            ),
            rx.hstack(
                rx.unordered_list(
                    rx.list_item("Liderazgo de proyectos end-to-end: desde cliente hasta arquitectura técnica"),
                    rx.list_item("Sistemas para hospitales medianos con alto nivel de complejidad"),
                    rx.list_item("Sistemas de almacén con seguridad avanzada y biometría"),
                    rx.list_item("Integración con servicios de terceros y APIs."),
                    rx.list_item("Cumplimiento normativo (SAT) y validación de lotes"),
                    class_name="list-disc pl-5 space-y-2",
                ),
            ),
        ),
        class_name="border border-solid border-yelow-300 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow duration-300",
    )
