from fastapi import FastAPI

from . import hello


def launch_backend(api: FastAPI):
    api.include_router(hello.router)
