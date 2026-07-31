from app.schemas.analytics import QuestionRankingRead

from app.services.analytics.frequency import (
    get_question_frequency,
)


def get_question_ranking(db):

    frequencies = get_question_frequency(db)

    return [

        QuestionRankingRead(
            question_id=item.question_id,
            question_text=item.question_text,
            frequency=item.frequency,
            importance_score=float(item.frequency),
        )

        for item in frequencies

    ]