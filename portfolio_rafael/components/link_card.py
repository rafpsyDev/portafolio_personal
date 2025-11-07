import reflex as rx

def link_card(label: str, href: str, icon_tag: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.icon(tag=icon_tag, class_name="text-yellow-500"),
            rx.text(label, high_contrast=True, class_name="ml-2"),
            class_name="items-center border border-solid border-yellow-300 rounded-lg p-4  transition-all duration-200 flex",
        ),
        href=href,
        is_external=True,
    )