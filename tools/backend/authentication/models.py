import datetime

import reflex as rx
import sqlalchemy
import sqlmodel


class User(rx.Model, table=True):
    provider_id: str
    email: str
    created_at: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "created_at",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        return d
