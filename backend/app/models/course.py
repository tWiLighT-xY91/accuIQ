from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.database import Base

from app.models.mixins import TimestampMixin


class Course(Base, TimestampMixin):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)

    course_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    course_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )

    semester: Mapped[int]

    branch: Mapped[str]

    university: Mapped[str]

    documents = relationship(
        "Document",
        back_populates="course",
        cascade="all, delete-orphan",
    )