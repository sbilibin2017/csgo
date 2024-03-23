from datetime import datetime
from sqlalchemy import BIGINT, FLOAT, TIMESTAMP
from sqlalchemy import String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        int: BIGINT,
        datetime: TIMESTAMP(timezone=False),
        str: String(),
        dict: JSONB,
        float: FLOAT,
    }

    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    update_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    @classmethod
    def get_fields_by_names(cls, field_names: list[str]) -> list:
        fields = []
        for name in field_names:
            if hasattr(cls, name):
                value = getattr(cls, name)
                fields.append(value)
        return fields
