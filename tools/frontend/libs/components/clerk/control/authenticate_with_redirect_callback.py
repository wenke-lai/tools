import reflex as rx


class AuthenticateWithRedirectCallback(rx.Component):
    library = "@clerk/clerk-react"
    tag = "AuthenticateWithRedirectCallback"


authenticate_with_redirect_callback = AuthenticateWithRedirectCallback.create
