from pydantic import BaseModel


class QuestionFrequencyRead(BaseModel):
    question_id: int
    question_text: str
    frequency: int


class QuestionHistoryRead(BaseModel):
    question_id: int
    question_text: str
    year_count: int
    years: list[int]


class QuestionRankingRead(BaseModel):
    question_id: int
    question_text: str
    frequency: int
    importance_score: float