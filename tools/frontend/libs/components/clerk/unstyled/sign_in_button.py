import reflex as rx


class SignInButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignInButton"


sign_in_button = SignInButton.create
