from pydantic import BaseModel


class StructuredQuestion(BaseModel):

    question_number: int

    subpart: str | None = None

    section: str |None = None

    marks: int | None = None

    question_text: str

    course_outcomes: list[str] = []

    question_type: str | None = None