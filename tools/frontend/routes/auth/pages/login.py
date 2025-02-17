import reflex as rx

from tools.frontend.libs.components import clerk

from ..layout import layout


@layout
def login():
    return rx.container(
        clerk.authentication.sign_in(),
    )
