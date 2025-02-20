from typing import Annotated

import structlog
from fastapi import APIRouter, Cookie, HTTPException

from .services import UserCommandFactory

logger = structlog.get_logger()

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login")
async def login(__session: Annotated[str | None, Cookie()] = None):
    if __session is None:
        raise HTTPException(status_code=401)

    register_command = UserCommandFactory.create_register_command(session=__session)
    try:
        user = register_command.execute()
        # todo: login flow
        return "ok"
    except Exception as e:
        raise HTTPException(400, str(e))
