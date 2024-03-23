from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class GameDB(Base):
    __tablename__ = 'game'

    game_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    begin_at: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    map_id: Mapped[int] = mapped_column(ForeignKey('map.map_id', ondelete='CASCADE'), nullable=False)
