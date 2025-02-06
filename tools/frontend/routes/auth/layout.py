import reflex as rx

from typing import Callable


def header():
    return (rx.heading("header"),)


def footer():
    return (rx.heading("footer"),)


def layout(main: Callable[[], rx.Component]) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.el.header(
                header(),
            ),
            rx.el.main(
                main(),
            ),
            rx.el.footer(
                footer(),
            ),
        )
    )
