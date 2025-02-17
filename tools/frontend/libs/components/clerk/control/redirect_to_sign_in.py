import reflex as rx


class RedirectToSignIn(rx.Component):
    library = "@clerk/clerk-react"
    tag = "RedirectToSignIn"


redirect_to_sign_in = RedirectToSignIn.create
