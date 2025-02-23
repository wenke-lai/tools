import structlog
from dotenv import load_dotenv
from fastapi import FastAPI
from structlog.processors import CallsiteParameter, CallsiteParameterAdder, JSONRenderer

from . import authentication, hello

load_dotenv()

structlog.configure(
    processors=[
        CallsiteParameterAdder(
            {
                CallsiteParameter.FILENAME,
                CallsiteParameter.FUNC_NAME,
                CallsiteParameter.LINENO,
            }
        ),
        JSONRenderer(),
    ],
    # logger_factory=structlog.stdlib.LoggerFactory(),
)


def launch_backend(api: FastAPI):
    api.include_router(hello.router)
    api.include_router(authentication.router)
