from pydantic import BaseModel, ConfigDict

from app.models.enums import (
    DocumentStatus,
    DocumentType,
)


class DocumentBase(BaseModel):
    course_id: int

    title: str

    storage_uri: str

    mime_type: str

    file_size: int

    checksum: str

    document_type: DocumentType

    status: DocumentStatus = DocumentStatus.UPLOADED

    exam_year: int | None = None

    pages: int | None = None

    processing_time_ms: int | None = None


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    title: str | None = None

    status: DocumentStatus | None = None

    exam_year: int | None = None

    pages: int | None = None

    processing_time_ms: int | None = None


class DocumentRead(DocumentBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )