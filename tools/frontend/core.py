import reflex as rx

from .routes import auth, dashboard
from .routes.index import index


class GuardState(rx.State):
    logged_in: bool = True

    def redirect_to_login(self):
        if not self.logged_in:
            return rx.redirect("/auth/login")
        return rx.redirect("/")


def launch_frontend(app: rx.App):
    app.add_page(index, route="/")
    app.add_page(auth.index, route="/auth", on_load=GuardState.redirect_to_login)
    app.add_page(auth.pages.login, route="/auth/login")
    app.add_page(dashboard.index, route="/dashboard")
