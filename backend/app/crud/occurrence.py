from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.occurrence import QuestionOccurrence
from app.schemas.occurrence import (
    OccurrenceCreate,
    OccurrenceUpdate,
)


def create_occurrence(
    db: Session,
    occurrence: OccurrenceCreate,
) -> QuestionOccurrence:

    db_occurrence = QuestionOccurrence(
        **occurrence.model_dump()
    )

    db.add(db_occurrence)
    db.commit()
    db.refresh(db_occurrence)

    return db_occurrence


def get_occurrence(
    db: Session,
    occurrence_id: int,
) -> QuestionOccurrence | None:

    statement = (
        select(QuestionOccurrence)
        .where(QuestionOccurrence.id == occurrence_id)
    )

    return db.scalar(statement)


def get_occurrences(
    db: Session,
):

    statement = (
        select(QuestionOccurrence)
        .order_by(QuestionOccurrence.created_at.desc())
    )

    return list(db.scalars(statement))


def update_occurrence(
    db: Session,
    db_occurrence: QuestionOccurrence,
    updates: OccurrenceUpdate,
) -> QuestionOccurrence:

    update_data = updates.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_occurrence,
            key,
            value,
        )

    db.commit()
    db.refresh(db_occurrence)

    return db_occurrence


def delete_occurrence(
    db: Session,
    db_occurrence: QuestionOccurrence,
):

    db.delete(db_occurrence)
    db.commit()