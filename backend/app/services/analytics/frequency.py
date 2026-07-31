from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.occurrence import QuestionOccurrence
from app.schemas.analytics import QuestionFrequencyRead


def get_question_frequency(
    db: Session,
) -> list[QuestionFrequencyRead]:

    statement = (
        select(
            Question.id,
            Question.question_text,
            func.count(QuestionOccurrence.id).label("frequency"),
        )
        .join(
            QuestionOccurrence,
            Question.id == QuestionOccurrence.question_id,
        )
        .group_by(
            Question.id,
            Question.question_text,
        )
        .order_by(
            func.count(QuestionOccurrence.id).desc()
        )
    )

    rows = db.execute(statement).all()

    return [
        QuestionFrequencyRead(
            question_id=row.id,
            question_text=row.question_text,
            frequency=row.frequency,
        )
        for row in rows
    ]