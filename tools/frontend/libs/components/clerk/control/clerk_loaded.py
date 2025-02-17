import reflex as rx


class ClerkLoaded(rx.Component):
    library = "@clerk/clerk-react"
    tag = "ClerkLoaded"


clerk_loaded = ClerkLoaded.create
