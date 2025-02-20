from typing import Callable

import reflex as rx

from .components import clerk


def context_provider(page: Callable[[], rx.Component]) -> rx.Component:
    def wrapper(*children, **props):
        return clerk.clerk_provider(
            page(*children, **props),
            publishable_key="pk_test_Y2hhbXBpb24tc2t1bmstOTguY2xlcmsuYWNjb3VudHMuZGV2JA",  # todo: enhance key
        )

    return wrapper
