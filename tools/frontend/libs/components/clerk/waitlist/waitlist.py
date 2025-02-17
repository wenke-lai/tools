import reflex as rx


class Waitlist(rx.Component):
    library = "@clerk/clerk-react"
    tag = "Waitlist"


waitlist = Waitlist.create
