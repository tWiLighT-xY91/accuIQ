from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.question import Question
from app.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
)


def create_question(
    db: Session,
    question: QuestionCreate,
) -> Question:

    db_question = Question(**question.model_dump())

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def get_question(
    db: Session,
    question_id: int,
) -> Question | None:

    statement = (
        select(Question)
        .where(Question.id == question_id)
    )

    return db.scalar(statement)


def get_questions(
    db: Session,
):

    statement = (
        select(Question)
        .order_by(Question.created_at.desc())
    )

    return list(db.scalars(statement))


def update_question(
    db: Session,
    db_question: Question,
    updates: QuestionUpdate,
) -> Question:

    update_data = updates.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_question,
            key,
            value,
        )

    db.commit()
    db.refresh(db_question)

    return db_question


def delete_question(
    db: Session,
    db_question: Question,
):

    db.delete(db_question)
    db.commit()