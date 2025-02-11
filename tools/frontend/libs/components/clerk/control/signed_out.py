import reflex as rx


class SignedOut(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignedOut"


signed_out = SignedOut.create
