from dotenv import load_dotenv
from fastapi import FastAPI

from . import authentication, hello

load_dotenv()


def launch_backend(api: FastAPI):
    api.include_router(hello.router)
    api.include_router(authentication.router)
