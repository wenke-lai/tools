import reflex as rx

from .models import User


class UserRepository:
    def get_user(self, provider_id: str) -> User:
        with rx.session() as session:
            statement = User.select().where(User.provider_id == provider_id)
            results = session.exec(statement)
            return results[0]

    def create_user(self, provider_id: str, email: str) -> User:
        with rx.session() as session:
            user = User(provider_id=provider_id, email=email)
            session.add(user)
            session.commit()
            session.refresh()
            return user
