import reflex as rx
from typing import List
def card_skill(title: str, subtitle: str, tags: List[str]):
    return rx.vstack(
        rx.flex(
            rx.heading(
                title,
                size="5",
                font_family="Montserrat",
                class_name="font-bold"
            ),
            rx.badge(
                subtitle,
                color_scheme="yellow",
                size="3",
                radius="large",
                font_family="GeistMono"
            ),
            class_name="mb-4 flex justify-between items-center w-full",
        ),
        rx.flex(
            *[rx.badge(tag, color_scheme="gray", high_contrast=True, variant="outline", radius="full", size="2", font_family="Montserrat") for tag in tags],
            class_name="gap-2 mt-4 flex-wrap",
        ),
        class_name="border border-solid border-yellow-300 shadow-xl  rounded-2xl p-6 m-2 w-full",
    )
