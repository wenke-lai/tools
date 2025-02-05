import reflex as rx

from rxconfig import config

from typing import Callable
from .layout import layout


class State(rx.State):
    """The app state."""

    ...


@layout
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to Reflex!", size="9"),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
    )
