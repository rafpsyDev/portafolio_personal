import reflex as rx

def availability_card() -> rx.Component:
    return rx.card(
        rx.heading("Disponibilidad  ", size="5", class_name="mb-4 text-2xl"),
        rx.text(
            "Actualmente estoy",
            rx.text.strong(" buscando nuevas oportunidades"),
            " como ingeniero de software full-stack. Estoy interesado en proyectos desafiantes que involucren arquitectura de sistemas, desarrollo de APIs y liderazgo técnico.",
            font_family="Montserrat",
            high_contrast=True,
            class_name="mt-4 text-base"
        ),
        rx.text("Preferencias de trabajo", font_family="Montserrat", class_name="mt-4 text-base"),
        rx.hstack(
            rx.unordered_list(
                rx.list_item("Remoto o híbrido"),
                rx.list_item("Remoto o híbrido"),
                rx.list_item("Equipos con cultura de aprendizaje"),
                class_name="list-disc text-base pl-5"
            ),
            class_name="mt-4"
        ),
        class_name="border border-solid border-yellow-300 rounded-2xl p-6 m-2 shadow-lg w-full",
    )