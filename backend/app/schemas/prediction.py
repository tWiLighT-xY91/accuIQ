from pydantic import BaseModel, ConfigDict


class QuestionPredictionRead(BaseModel):
    """
    Represents the predicted importance of a question.
    """

    question_id: int

    question_text: str

    frequency: int

    year_count: int

    years: list[int]

    latest_year: int | None

    prediction_score: float

    confidence: str

    model_config = ConfigDict(from_attributes=True)
