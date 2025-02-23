import os

import jwt
import structlog
from clerk_backend_api import Clerk, models
from jwt import PyJWK, PyJWKClient
from pydantic import BaseModel

logger = structlog.get_logger()

CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY")


def get_jwks(token: str) -> tuple[PyJWK, str]:
    url = "https://api.clerk.com/v1/jwks"
    headers = {
        "Authorization": f"Bearer {CLERK_SECRET_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    }

    client = PyJWKClient(url, headers=headers)
    signing_key = client.get_signing_key_from_jwt(token=token)
    return signing_key, "RS256"


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
    signing_key, algorithm = get_jwks(session_token)
    payload = jwt.decode(session_token, signing_key, algorithms=[algorithm])
    return ClerkSessionToken(**payload)


def get_user_info(user_id: str) -> models.User | None:
    with Clerk(bearer_auth=CLERK_SECRET_KEY) as clerk:
        user = clerk.users.get(user_id=user_id)
        logger.info("info", user=user)
        return user


"""
def revoke_session(session_id: str):
    clerk = get_clerk(CLERK_SECRET_KEY)
    clerk.sessions.revoke(session_id=session_id)
"""
