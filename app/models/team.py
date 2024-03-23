from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class TeamDB(Base):
    __tablename__ = 'team'

    team_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    team_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(default='', nullable=False, unique=False)
    location: Mapped[str] = mapped_column(default='', nullable=False, unique=False)
