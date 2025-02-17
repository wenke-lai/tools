import reflex as rx


class ClerkLoading(rx.Component):
    library = "@clerk/clerk-react"
    tag = "ClerkLoading"


clerk_loading = ClerkLoading.create
