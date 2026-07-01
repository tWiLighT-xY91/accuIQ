from pydantic import BaseModel, ConfigDict


class OccurrenceBase(BaseModel):
    question_id: int

    document_id: int

    question_number: int

    page_number: int

    marks: int


class OccurrenceCreate(OccurrenceBase):
    pass


class OccurrenceUpdate(BaseModel):
    question_number: int | None = None

    page_number: int | None = None

    marks: int | None = None


class OccurrenceRead(OccurrenceBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )