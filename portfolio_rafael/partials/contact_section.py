import reflex as rx
from ..components.link_card import link_card
from ..components.contact_links_card import contact_links_card
from ..components.availability_card import availability_card

def contact_section() -> rx.Component:
    return rx.box(
        rx.blockquote(
            "Contacto",
            size="7", 
            class_name="mb-8 mt-8", 
            font_family="Gotham-Black", 
            color_scheme="yellow"
        ),
        rx.text(
            "Estoy abierto a nuevas oportunidades laborales. Si buscas un ingeniero de software con experiencia en sistemas complejos y liderazgo técnico, hablemos.", 
            size="4", 
            class_name="mb-4",
            font_family="Montserrat"
        ),
        rx.box(
            contact_links_card(),
            availability_card(),
            class_name="w-full flex flex-col md:flex-row"
            ),
        class_name="w-full "
    )