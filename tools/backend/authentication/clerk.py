import os
from functools import lru_cache
from typing import TYPE_CHECKING

import jwt
import structlog
from clerk_backend_api import Clerk
from pydantic import BaseModel

if TYPE_CHECKING:
    from clerk_backend_api.models import Keys, User


logger = structlog.get_logger()

CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY")


@lru_cache
def get_clerk(bearer_auth: str) -> Clerk:
    logger.info("called `get_clerk()`")

    return Clerk(bearer_auth)


@lru_cache
def get_jwks(bearer_auth: str) -> Keys:
    logger.info("called `get_jwks()`")

    clerk = get_clerk(bearer_auth)
    response = clerk.jwks.get()
    return response.keys[0]


class ClerkSessionToken(BaseModel):
    """Clerk session token

    NOTE: skip `actor` and `organization` claims for now

    ref: https://clerk.com/docs/backend-requests/resources/session-tokens
    """

    azp: str  # authorized party

    exp: int  # expiration time (RFC 7519)

    iat: int  # issued at (RFC 7519)

    iss: str  # issuer

    nbf: int  # not before (RFC 7519)

    sid: str  # session id - the id of the current session

    sub: str  # subject - the id of the current user of the session


def decode_session_token(session_token: str) -> ClerkSessionToken:
    # todo: should we cache this token?

    key = get_jwks(CLERK_SECRET_KEY)  # cache
    payload = jwt.decode(session_token, key.n, algorithms=[key.alg])
    return ClerkSessionToken(**payload)


def revoke_session(session_id: str):
    clerk = get_clerk(CLERK_SECRET_KEY)
    clerk.sessions.revoke(session_id=session_id)


def get_user(user_id: str) -> User:
    clerk = get_clerk(CLERK_SECRET_KEY)
    return clerk.users.get(user_id=user_id)
