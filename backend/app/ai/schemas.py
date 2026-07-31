from pydantic import BaseModel
from pydantic import field_validator

class StructuredQuestion(BaseModel):

    question_number: int

    subpart: str | None = None

    section: str |None = None

    marks: int | None = None

    question_text: str

    course_outcomes: list[str] | None = None

    question_type: str | None = None
    

class DocumentMetadataAI(BaseModel):
    exam_year: int | None = None