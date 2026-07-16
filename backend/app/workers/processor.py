from sqlalchemy.orm import Session

from app.crud.document import (
    get_document,
    update_document,
)

from app.models.enums import DocumentStatus

from app.schemas.document import DocumentUpdate

from app.services.processing.pipeline import process_document


def process_document_worker(
    db: Session,
    document_id: int,
):
    document = get_document(
        db,
        document_id,
    )
    if document is None:
        return
    update_document(
        db,
        document,
        DocumentUpdate(
            status=DocumentStatus.PROCESSING,
        ),
    )
    process_document(
        document,
    )
    update_document(
        db,
        document,
        DocumentUpdate(
            status=DocumentStatus.PROCESSED,
        ),
    )
