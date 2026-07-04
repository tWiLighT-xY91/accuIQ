from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.crud.question import (
    create_question,
    get_question,
    get_questions,
    update_question,
    delete_question,
)

from app.schemas.question import (
    QuestionCreate,
    QuestionRead,
    QuestionUpdate,
)

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)

@router.post(
    "/",
    response_model=QuestionRead,
    status_code=201,
)
def create_new_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
):
    return create_question(
        db,
        question,
    )
    
@router.get(
    "/",
    response_model=list[QuestionRead],
)
def read_questions(
    db: Session = Depends(get_db),
):
    return get_questions(db)

@router.get(
    "/{question_id}",
    response_model=QuestionRead,
)
def read_question(
    question_id: int,
    db: Session = Depends(get_db),
):
    question = get_question(
        db,
        question_id,
    )

    if question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found",
        )

    return question

@router.put(
    "/{question_id}",
    response_model=QuestionRead,
)
def update_existing_question(
    question_id: int,
    updates: QuestionUpdate,
    db: Session = Depends(get_db),
):
    question = get_question(
        db,
        question_id,
    )

    if question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found",
        )

    return update_question(
        db,
        question,
        updates,
    )
    
@router.delete(
    "/{question_id}",
    status_code=204,
)
def delete_existing_question(
    question_id: int,
    db: Session = Depends(get_db),
):
    question = get_question(
        db,
        question_id,
    )

    if question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found",
        )

    delete_question(
        db,
        question,
    )
    
