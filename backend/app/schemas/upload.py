from pydantic import BaseModel

from app.models.enums import DocumentType


class UploadRequest(BaseModel):
    course_id: int
    document_type: DocumentType
    exam_year: int | None = None