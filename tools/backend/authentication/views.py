from typing import Annotated

import structlog
from fastapi import APIRouter, Cookie, HTTPException, Response, status

from .services import UserService

logger = structlog.get_logger()

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(__session: Annotated[str, Cookie()], response: Response):
    try:
        service = UserService()
        access_token, created = service.login(__session)
        if created:
            response.status_code = status.HTTP_201_CREATED
        return {"access_token": access_token}
    except Exception as e:
        raise HTTPException(400, str(e))


@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(__session: Annotated[str, Cookie()]):
    try:
        service = UserService()
        service.logout(__session)
        return
    except Exception as e:
        raise HTTPException(400, str(e))
