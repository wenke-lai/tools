import structlog

from . import clerk
from .models import User
from .repositories import UserRepository

logger = structlog.get_logger()


class Notification:
    def send(self, subject, message):
        logger.info("send notification", subject, message)


class UserService:
    def __init__(self, notification):
        self.repository = UserRepository()
        self.notification = notification

    def register(self, session: str) -> User:
        info = clerk.get_user_info(session)
        user = self.repository.create_user(info)
        self.notification.send(user.username, "welcome")
        return user

    def login(self, session: str) -> tuple[str, bool]:
        created = False
        token = clerk.decode_session_token(session)
        user = self.repository.get_user(provider_id=token.sub)

        # create the user
        if not user:
            user = self.register(user_id=token.sub)
            created = True

        access_token = self.repository.login_user(user_id=user.id)
        return access_token, created

    def logout(self, session: str) -> None:
        token = clerk.decode_session_token(session)
        self.repository.revoke_access_token(user_id=token.sub)
