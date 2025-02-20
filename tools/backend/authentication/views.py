from typing import Annotated

from fastapi import APIRouter, Cookie, HTTPException

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login")
async def login(__session: Annotated[str | None, Cookie()] = None):
    if __session is None:
        raise HTTPException(status_code=401)
    return "ok"
