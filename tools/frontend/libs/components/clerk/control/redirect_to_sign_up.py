import reflex as rx


class RedirectToSignUp(rx.Component):
    library = "@clerk/clerk-react"
    tag = "RedirectToSignUp"


redirect_to_sign_up = RedirectToSignUp.create
