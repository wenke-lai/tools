from typing import Callable

import reflex as rx

from tools.frontend.libs.components import clerk


def header() -> rx.Component:
    return rx.el.header(
        rx.heading("Header"),
        class_name="min-h-16 p-4",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.heading("Footer"),
        rx.text(
            "© 2024 Arcstratus All Rights Reserved.",
            class_name="opacity-60",
        ),
        class_name=[
            # layout
            "absolute bottom-0 inset-x-0",
            # spacing and typography
            "p-4 text-center",
        ],
    )


def main(children: Callable[[], rx.Component]) -> rx.Component:
    return rx.el.main(
        children(),
    )


def layout(children: Callable[[], rx.Component]) -> rx.Component:
    return clerk.clerk_provider(
        rx.container(
            rx.vstack(
                header(),
                main(children),
                footer(),
                class_name="items-center",
            ),
        ),
        publishable_key="pk_test_123",  # todo: enhance key
    )
