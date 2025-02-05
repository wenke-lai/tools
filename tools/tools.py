"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .backend.manage import launch_backend
from .frontend.core import launch_frontend

app = rx.App()

launch_frontend(app)

launch_backend(app.api)
