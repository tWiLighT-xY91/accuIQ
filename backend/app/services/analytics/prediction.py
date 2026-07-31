from sqlalchemy.orm import Session

from app.core.prediction_config import (
    FREQUENCY_WEIGHT,
    YEAR_COVERAGE_WEIGHT,
    RECENCY_WEIGHT,
    HIGH_CONFIDENCE_THRESHOLD,
    MEDIUM_CONFIDENCE_THRESHOLD,
)

from app.schemas.prediction import QuestionPredictionRead

from app.services.analytics.frequency import get_question_frequency
from app.services.analytics.history import get_question_history


def get_question_predictions(
    db: Session,
) -> list[QuestionPredictionRead]:
    """
    Computes prediction scores for all questions using
    historical frequency and year coverage.

    Prediction Score =
        0.6 * normalized_frequency
      + 0.4 * normalized_year_coverage
    """

    frequency_data = get_question_frequency(db)
    history_data = get_question_history(db)

    history_lookup = {
        item.question_id: item
        for item in history_data
    }

    if not frequency_data:
        return []

    max_frequency = max(
        item.frequency
        for item in frequency_data
    )

    max_year_count = max(
        (
            history_lookup[item.question_id].year_count
            for item in frequency_data
            if item.question_id in history_lookup
        ),
        default=1,
    )

    predictions: list[QuestionPredictionRead] = []

    for frequency_item in frequency_data:

        history_item = history_lookup.get(
            frequency_item.question_id
        )

        if history_item is None:
            continue

        normalized_frequency = (
            frequency_item.frequency / max_frequency
            if max_frequency
            else 0.0
        )

        normalized_year_count = (
            history_item.year_count / max_year_count
            if max_year_count
            else 0.0
        )

        prediction_score = (
            normalized_frequency * FREQUENCY_WEIGHT
            + normalized_year_count * YEAR_COVERAGE_WEIGHT
        )

        if prediction_score >= HIGH_CONFIDENCE_THRESHOLD:
            confidence = "High"

        elif prediction_score >= MEDIUM_CONFIDENCE_THRESHOLD:
            confidence = "Medium"

        else:
            confidence = "Low"

        predictions.append(
            QuestionPredictionRead(
                question_id=frequency_item.question_id,
                question_text=frequency_item.question_text,
                frequency=frequency_item.frequency,
                year_count=history_item.year_count,
                years=history_item.years,
                latest_year=max(history_item.years)
                if history_item.years
                else None,
                prediction_score=round(
                    prediction_score,
                    3,
                ),
                confidence=confidence,
            )
        )

    predictions.sort(
        key=lambda prediction: prediction.prediction_score,
        reverse=True,
    )

    return predictions