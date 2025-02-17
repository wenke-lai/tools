import reflex as rx


class SignUpButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignUpButton "


sign_up_button = SignUpButton.create
