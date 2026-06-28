from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.occurrence import QuestionOccurrence


class Question(Base, TimestampMixin):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)

    question_text: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    normalized_hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
    )

    occurrences: Mapped[list["QuestionOccurrence"]] = relationship(
        back_populates="question",
        cascade="all, delete-orphan",
    )