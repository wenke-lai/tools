import reflex as rx


class SignIn(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignIn"


sign_in = SignIn.create
