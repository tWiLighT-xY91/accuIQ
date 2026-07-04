from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.crud.document import (
    create_document,
    get_document,
    get_documents,
    update_document,
    delete_document,
)

from app.schemas.document import (
    DocumentCreate,
    DocumentRead,
    DocumentUpdate,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post(
    "/",
    response_model=DocumentRead,
    status_code=201,
)
def create_new_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
):
    return create_document(
        db,
        document,
    )
    
@router.get(
    "/",
    response_model=list[DocumentRead],
)
def read_documents(
    db: Session = Depends(get_db),
):
    return get_documents(db)

@router.get(
    "/{document_id}",
    response_model=DocumentRead,
)
def read_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document

@router.put(
    "/{document_id}",
    response_model=DocumentRead,
)
def update_existing_document(
    document_id: int,
    updates: DocumentUpdate,
    db: Session = Depends(get_db),
):
    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return update_document(
        db,
        document,
        updates,
    )

@router.delete(
    "/{document_id}",
    status_code=204,
)
def delete_existing_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    delete_document(
        db,
        document,
    )
