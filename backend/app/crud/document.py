from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
)


def create_document(
    db: Session,
    document: DocumentCreate,
) -> Document:

    db_document = Document(**document.model_dump())

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document


def get_document(
    db: Session,
    document_id: int,
) -> Document | None:

    statement = select(Document).where(Document.id == document_id)

    return db.scalar(statement)


def get_documents(
    db: Session,
):

    statement = select(Document).order_by(Document.created_at.desc())

    return list(db.scalars(statement))


def update_document(
    db: Session,
    db_document: Document,
    updates: DocumentUpdate,
) -> Document:

    update_data = updates.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(
            db_document,
            key,
            value,
        )

    db.commit()
    db.refresh(db_document)

    return db_document


def delete_document(
    db: Session,
    db_document: Document,
):

    db.delete(db_document)
    db.commit()
