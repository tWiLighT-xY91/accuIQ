from pydantic import BaseModel, ConfigDict


class QuestionBase(BaseModel):
    question_text: str
    normalized_hash: str


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):
    question_text: str | None = None


class QuestionRead(QuestionBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )