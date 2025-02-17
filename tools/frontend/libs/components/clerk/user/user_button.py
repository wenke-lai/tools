import reflex as rx


class UserButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "UserButton"


user_button = UserButton.create
