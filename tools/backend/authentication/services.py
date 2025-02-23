import structlog
from clerk_backend_api.models import SDKError
from jwt.exceptions import PyJWTError

from . import clerk
from .models import User
from .repositories import UserRepository

logger = structlog.get_logger()


class ServiceError(Exception):
    pass


class BadGatewayError(ServiceError):
    pass


class Notification:
    def send(self, subject, message):
        logger.info("send notification", subject, message)


class UserService:
    def __init__(self, notification: Notification | None = None):
        self.repository = UserRepository()
        self.notification = notification

    def register(self, user_id: str) -> User:
        logger.debug("user register", user_id=user_id)
        info = clerk.get_user_info(user_id)
        user = self.repository.create(info)

        if self.notification:
            self.notification.send(user.username, "welcome")
        return user

    def login(self, session_token: str) -> tuple[str, bool]:
        logger.debug("user login", sessiont_token=session_token)
        try:
            clerk_session_token = clerk.decode_session_token(session_token)
            user = self.repository.retrieve(provider_user_id=clerk_session_token.sub)

            # Get or Create
            created = False
            if user is None:
                created = True
                user = self.register(clerk_session_token.sub)

            access_token = self.repository.login(user)
            return access_token, created

        except SDKError as exc:
            event = "Clerk API error occurred"
            logger.exception(event, exc_info=exc)
            raise BadGatewayError(event)

        except PyJWTError as exc:
            event = "Invalid session token"
            logger.exception(event, exc_info=exc)
            raise BadGatewayError(event)

    def logout(self, session_token: str) -> None:
        token = clerk.decode_session_token(session_token)
        self.repository.logout()
