from fastapi import FastAPI

from . import authentication, hello


def launch_backend(api: FastAPI):
    api.include_router(hello.router)
    api.include_router(authentication.router)
