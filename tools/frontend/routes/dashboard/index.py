import reflex as rx

from tools.frontend.libs.components import clerk

from .layout import layout


@layout
def index():
    return rx.container(
        rx.heading("welcome"),
        clerk.control.signed_in(
            rx.text("status: logged in"),
            rx.button(
                clerk.unstyled.sign_out_button(),
            ),
        ),
        clerk.control.signed_out(
            rx.text("status: logged out"),
            rx.button(
                clerk.unstyled.sign_in_button(),
            ),
        ),
    )
