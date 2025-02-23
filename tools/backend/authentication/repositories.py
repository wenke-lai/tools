import reflex as rx

from .models import User
import structlog

logger = structlog.get_logger()


class UserRepository:
    def create(self, data) -> User:
        with rx.session() as session:
            user = User(
                provider_user_id=data.id,
                email=data.email_addresses[0].email_address,
                username=data.username or data.first_name,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def retrieve(self, provider_user_id: str) -> User | None:
        with rx.session() as session:
            stmt = User.select().where(User.provider_user_id == provider_user_id)
            return session.scalars(stmt).first()

    def login(self, user: User) -> str:
        return "access-token"

    def logout(self, access_token: str) -> None:
        return
