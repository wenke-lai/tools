import reflex as rx


from typing import Callable


def layout(main: Callable[[], rx.Component]) -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        main(),
        rx.logo(),
    )
