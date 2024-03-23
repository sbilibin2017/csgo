from uuid import uuid4

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class StatisticDB(Base):
    __tablename__ = 'statistic'

    statistic_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_id: Mapped[int] = mapped_column(ForeignKey('game.game_id', ondelete='CASCADE'), nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey('player.player_id', ondelete='CASCADE'), nullable=False)
    kills: Mapped[int] = mapped_column(nullable=False, unique=True)
    deaths: Mapped[int] = mapped_column(nullable=False, unique=True)
    assists: Mapped[int] = mapped_column(nullable=False, unique=True)
    headshots: Mapped[int] = mapped_column(nullable=False, unique=True)
    flash_assists: Mapped[int] = mapped_column(nullable=False, unique=True)
    first_kills_diff: Mapped[int] = mapped_column(nullable=False, unique=True)
    k_d_diff: Mapped[int] = mapped_column(nullable=False, unique=True)
    adr: Mapped[float] = mapped_column(nullable=False, unique=True)
    kast: Mapped[float] = mapped_column(nullable=False, unique=True)
    rating: Mapped[float] = mapped_column(nullable=False, unique=True)
