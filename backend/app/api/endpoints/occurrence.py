from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.crud.occurrence import (
    create_occurrence,
    get_occurrence,
    get_occurrences,
    update_occurrence,
    delete_occurrence,
)

from app.schemas.occurrence import (
    OccurrenceCreate,
    OccurrenceRead,
    OccurrenceUpdate,
)

router = APIRouter(
    prefix="/occurrences",
    tags=["Occurrences"],
)

@router.post(
    "/",
    response_model=OccurrenceRead,
    status_code=201,
)
def create_new_occurrence(
    occurrence: OccurrenceCreate,
    db: Session = Depends(get_db),
):
    return create_occurrence(
        db,
        occurrence,
    )
    
@router.get(
    "/",
    response_model=list[OccurrenceRead],
)
def read_occurrences(
    db: Session = Depends(get_db),
):
    return get_occurrences(db)

@router.get(
    "/{occurrence_id}",
    response_model=OccurrenceRead,
)
def read_occurrence(
    occurrence_id: int,
    db: Session = Depends(get_db),
):
    occurrence = get_occurrence(
        db,
        occurrence_id,
    )

    if occurrence is None:
        raise HTTPException(
            status_code=404,
            detail="Occurrence not found",
        )

    return occurrence

@router.put(
    "/{occurrence_id}",
    response_model=OccurrenceRead,
)
def update_existing_occurrence(
    occurrence_id: int,
    updates: OccurrenceUpdate,
    db: Session = Depends(get_db),
):
    occurrence = get_occurrence(
        db,
        occurrence_id,
    )

    if occurrence is None:
        raise HTTPException(
            status_code=404,
            detail="Occurrence not found",
        )

    return update_occurrence(
        db,
        occurrence,
        updates,
    )
    
@router.delete(
    "/{occurrence_id}",
    status_code=204,
)
def delete_existing_occurrence(
    occurrence_id: int,
    db: Session = Depends(get_db),
):
    occurrence = get_occurrence(
        db,
        occurrence_id,
    )

    if occurrence is None:
        raise HTTPException(
            status_code=404,
            detail="Occurrence not found",
        )

    delete_occurrence(
        db,
        occurrence,
    )
    
