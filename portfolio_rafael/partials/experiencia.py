import reflex as rx
from ..components.experience_card import card_xp
from ..data.experience_data import experiencia


def experiencia_section() ->rx.Component:
    return rx.box(
        rx.blockquote(
            "Experiencia",
            size="7", 
            class_name="mb-8 mt-8", 
            font_family="Gotham-Black", 
            color_scheme="yellow"
            ),
        rx.vstack(
            *[card_xp(**exp) for exp in experiencia],  
            class_name="w-full space-y-4 gap-4",
        ),
        class_name="w-full "
    )