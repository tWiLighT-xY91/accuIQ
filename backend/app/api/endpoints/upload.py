from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
)
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.crud.document import create_document

from app.models.enums import DocumentType

from app.schemas.document import (
    DocumentCreate,
    DocumentRead,
)

from app.services.upload.uploader import upload_document

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post(
    "/",
    response_model=DocumentRead,
    status_code=201,
)
async def upload_file(
    file: UploadFile = File(...),
    course_id: int = Form(...),
    document_type: DocumentType = Form(...),
    exam_year: int | None = Form(None),
    db: Session = Depends(get_db),
):
    """
    Upload a document and create its database entry.
    """

    try:
        upload_result = await upload_document(file)

    except ValueError as e:
        raise HTTPException(
            status_code=415,
            detail=str(e),
        )

    document = create_document(
        db,
        DocumentCreate(
            course_id=course_id,
            title=Path(file.filename).stem,
            storage_uri=upload_result.storage_uri,
            mime_type=upload_result.mime_type,
            file_size=upload_result.file_size,
            checksum="pending",
            document_type=document_type,
            exam_year=exam_year,
        ),
    )

    return document
