import reflex as rx


class Protect(rx.Component):
    library = "@clerk/clerk-react"
    tag = "Protect"


protect = Protect.create
