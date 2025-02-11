import reflex as rx


class SignedIn(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignedIn"


signed_in = SignedIn.create
