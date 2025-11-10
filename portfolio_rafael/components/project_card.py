import reflex as rx

def project_card(image: str, title: str, description: str, features: list[str], technologies: list[str]) -> rx.Component:
    return rx.card(
        rx.image(
            src=image,
            class_name="w-full h-48 object-cover rounded-t-md",
        ),
        rx.box(
            rx.heading(title),
            rx.text(description, class_name="mt-2 text-base"),
        ),
        rx.box(
            rx.heading("Características principales", size="3", class_name="mt-3"),
            rx.unordered_list(*[rx.list_item(f) for f in features], class_name="mt-2 text-sm"),
        ),
        rx.box(
            rx.heading("Tecnologías", size="3", class_name="mt-3"),
            rx.flex(
                *[rx.badge(t, color_scheme="yellow", variant="soft") for t in technologies],
                class_name="flex flex-wrap gap-2 mt-2 text-sm",
            ),
        ),
        class_name="p-4"
    )