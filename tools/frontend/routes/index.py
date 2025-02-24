import httpx
import reflex as rx

from rxconfig import config

from .layout import layout


class State(rx.State):
    """The app state."""

    session: str = rx.Cookie(name="__session")
    access_token: str = rx.Cookie(name="access_token")

    data: dict = {}

    @rx.event(background=True)
    async def auth(self):
        async with self:
            url = "http://localhost:8000/auth/login"
            async with httpx.AsyncClient() as client:
                response = await client.post(url, cookies={"__session": self.session})
                print("---", response.cookies)
                self.access_token = response.cookies["access_token"]
                self.data = response.json()


@layout
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to Reflex!", size="9"),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        rx.button("dashboard", on_click=rx.redirect("/dashboard")),
        # todo: remove me, debug only
        rx.box(
            rx.text(
                State.session,
                class_name="text-3xl text-red-500 max-w-3xl max-h-32 overflow-auto",
            ),
            rx.button("auth", on_click=State.auth),
            rx.text(State.data),
            class_name="border border-sky-400 p-4 rounded space-y-4",
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
    )
