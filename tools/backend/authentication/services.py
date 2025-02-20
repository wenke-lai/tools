from abc import ABC, abstractmethod
from dataclasses import dataclass

from . import clerk
from .models import User


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


@dataclass
class RegisterUserCommand(Command):
    session: str

    def __init__(self, repository, notification, logger):
        self.repository = repository
        self.notification = notification
        self.logger = logger

    def execute(self) -> User:
        user_data = clerk.get_user(self.session)
        user = self.repository.create_user(**user_data)

        self.notification.send_welcome_email(user.email)

        self.logger.info(user.id, "registered")
        return user


class UserCommandFactory:
    def __init__(self, repository, notification, logger):
        self.repository = repository
        self.notification = notification
        self.logger = logger

    def create_register_command(self, session: str) -> RegisterUserCommand:
        cmd = RegisterUserCommand(self.repository, self.notification, self.logger)
        cmd.session = session
        return cmd
