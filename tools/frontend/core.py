import reflex as rx

from .routes.index import index
from .routes import auth


class GuardState(rx.State):
    logged_in: bool = True

    def redirect_to_login(self):
        if not self.logged_in:
            return rx.redirect("/auth/login")
        return rx.redirect("/")


def launch_frontend(app: rx.App):
    app.add_page(index, route="/")
    app.add_page(auth.index, route="/auth", on_load=GuardState.redirect_to_login)
    app.add_page(auth.login, route="/auth/login")
