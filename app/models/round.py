from uuid import uuid4

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class RoundDB(Base):
    __tablename__ = 'round'

    round_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_id: Mapped[int] = mapped_column(ForeignKey('game.game_id', ondelete='CASCADE'), nullable=False)
    ct_id: Mapped[int] = mapped_column(ForeignKey('team.team_id', ondelete='CASCADE'), nullable=False)
    t_id: Mapped[int] = mapped_column(ForeignKey('team.team_id', ondelete='CASCADE'), nullable=False)
    winner_id: Mapped[int] = mapped_column(ForeignKey('team.team_id', ondelete='CASCADE'), nullable=False)
    round: Mapped[int] = mapped_column(nullable=False, unique=True)
    outcome: Mapped[str] = mapped_column(nullable=False, unique=False)
