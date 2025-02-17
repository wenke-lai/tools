import reflex as rx


class SignInWithMetamaskButton(rx.Component):
    library = "@clerk/clerk-react"
    tag = "SignInWithMetamaskButton"


sign_in_with_metamask_button = SignInWithMetamaskButton.create
