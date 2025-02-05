from reflex import App

from .routes.index import index


def launch_frontend(app: App):
    app.add_page(index)
