import reflex as rx

from ..layout import layout


class LoginState(rx.State):

    @rx.event
    def on_submit(self, form_data: dict):
        print(form_data)


@layout
def login():
    return rx.form(
        rx.vstack(
            rx.text("Email:"),
            rx.input(
                placeholder="example@email.com",
                name="email",
                type="email",
                class_name="w-full",
            ),
            rx.text("Password:"),
            rx.input(
                placeholder="********",
                name="password",
                type="password",
                class_name="w-full",
            ),
            rx.button("Login", type="submit"),
        ),
        on_submit=LoginState.on_submit,
        reset_on_submit=True,
    )
