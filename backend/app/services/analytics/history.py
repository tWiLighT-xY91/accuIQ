from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.question import Question
from app.models.occurrence import QuestionOccurrence

from app.schemas.analytics import QuestionHistoryRead


def get_question_history(
    db: Session,
) -> list[QuestionHistoryRead]:

    statement = (
        select(
            Question.id,
            Question.question_text,
            Document.exam_year,
        )
        .join(
            QuestionOccurrence,
            Question.id == QuestionOccurrence.question_id,
        )
        .join(
            Document,
            Document.id == QuestionOccurrence.document_id,
        )
    )

    rows = db.execute(statement).all()

    history = {}

    for row in rows:

        if row.id not in history:

            history[row.id] = {
                "question_text": row.question_text,
                "years": [],
            }

        if (
            row.exam_year is not None
            and row.exam_year not in history[row.id]["years"]
        ):
            history[row.id]["years"].append(row.exam_year)

    result = []

    for question_id, data in history.items():

        years = sorted(data["years"])

        result.append(
            QuestionHistoryRead(
                question_id=question_id,
                question_text=data["question_text"],
                frequency=len(years),
                years=years,
            )
        )

    return result