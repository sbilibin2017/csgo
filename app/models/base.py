from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    update_date: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    @classmethod
    def get_fields_by_names(cls, field_names: list[str]) -> list:
        fields = []
        for name in field_names:
            if hasattr(cls, name):
                value = getattr(cls, name)
                fields.append(value)
        return fields
