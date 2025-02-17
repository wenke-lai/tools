import reflex as rx


class SignUp(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignUp"


sign_up = SignUp.create
