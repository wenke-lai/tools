import reflex as rx


class GoogleOneTap(rx.Component):
    library = "@clerk/clerk-react"
    tag = "GoogleOneTap"


google_one_tap = GoogleOneTap.create
