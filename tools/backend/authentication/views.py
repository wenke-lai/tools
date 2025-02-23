from typing import Annotated

import structlog
from fastapi import APIRouter, Cookie, HTTPException, Response, status

from .services import BadGatewayError, UserService

logger = structlog.get_logger()

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(__session: Annotated[str, Cookie()], response: Response):
    try:
        session = UserService()
        access_token, created = session.login(session_token=__session)
        logger.info("Login success", access_token=access_token)

        if created:
            response.status_code = status.HTTP_201_CREATED
        response.set_cookie(key="access_token", value=access_token)
        return {"msg": "ok"}
    except BadGatewayError as exc:
        logger.exception("Bad gateway", exc_info=exc)
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc))
    except Exception as exc:
        logger.exception("Exception", exc_info=exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)
        )


@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(__session: Annotated[str, Cookie()]):
    try:
        service = UserService()
        service.logout(session_token=__session)
        logger.info("logout success")

        return
    except Exception as exc:
        logger.exception("Exception", exc_info=exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)
        )
