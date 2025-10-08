import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.vstack(
                rx.heading("Portafolio Rafael Eduardo Rosales Rivas", class_name="text-4xl font-bold text-teal-400"),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
    )


app = rx.App()
app.add_page(index)
