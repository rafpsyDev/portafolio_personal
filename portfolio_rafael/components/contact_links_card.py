import reflex as rx
from .link_card import link_card

def contact_links_card() -> rx.Component:
    return rx.card(
        rx.heading("Conectremos", size="5", class_name="mb-8 text-2xl"),
        rx.vstack(
            rx.hstack(
                link_card(
                    label="rafael_ed@proton.me",
                    href="mailto:rafael_ed@proton.me",
                    icon_tag="mail",
                ),
            ),
            rx.hstack(
                link_card(
                    label="Github",
                    href="https://github.com/rafpsyDev",
                    icon_tag="github",
                ),
            ),
            rx.hstack(
                link_card(
                    label="Linkedin",
                    href="https://www.linkedin.com/in/rafael-rosales-dev/",
                    icon_tag="linkedin",
                ),
                class_name="mb-6"
            ),
        ),
        class_name="border border-solid border-yellow-300 rounded-2xl p-6 m-2 shadow-lg w-full h-full",
    )