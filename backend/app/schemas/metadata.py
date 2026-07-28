from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    exam_year: int | None = None

    course_code: str | None = None

    course_name: str | None = None

    semester: str | None = None

    exam_type: str | None = None

    institution: str | None = None