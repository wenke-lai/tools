from typing import Callable

from tools.frontend.libs.context import context_provider
from tools.frontend.libs.components import clerk

import reflex as rx


def text_animation(text: str):
    return rx.box(
        rx.text(
            text,
            class_name="text-xl text-[#9CA3AF] group-hover:text-white capitalize",
        ),
        rx.el.span(
            class_name=[
                "absolute -bottom-1 inset-x-0 h-0.5 bg-white transition-all duration-300 ease-in-out",
                "w-0 group-hover:w-full",
            ]
        ),
        class_name=["relative", "group"],
    )


def header():
    return rx.hstack(
        text_animation("Product"),
        text_animation("API"),
        text_animation("Blog"),
        text_animation("About"),
        text_animation("Careers"),
    )


@context_provider
def layout(main: Callable[[], rx.Component]) -> rx.Component:
    return rx.container(
        header(),
        rx.color_mode.button(position="top-right"),
        main(),
        rx.logo(),
        clerk.control.signed_in(rx.text("logged in")),
        clerk.control.signed_out(rx.text("known")),
    )
