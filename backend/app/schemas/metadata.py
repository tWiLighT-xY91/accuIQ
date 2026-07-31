from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    exam_year: int | None = None