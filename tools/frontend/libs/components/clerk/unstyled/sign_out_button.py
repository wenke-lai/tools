import reflex as rx


class SignOutButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignOutButton "


sign_out_button = SignOutButton.create
