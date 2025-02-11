import reflex as rx


class ClerkProvider(rx.Component):
    library = "@clerk/clerk-react"

    tag = "ClerkProvider"

    publishable_key: rx.Var[str]


provider = ClerkProvider.create
