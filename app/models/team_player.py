from uuid import uuid4

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class TeamPlayerDB(Base):
    __tablename__ = 'team_player'

    team_player_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    game_id: Mapped[int] = mapped_column(ForeignKey('game.game_id', ondelete='CASCADE'), nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey('team.team_id', ondelete='CASCADE'), nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey('player.player_id', ondelete='CASCADE'), nullable=False)
