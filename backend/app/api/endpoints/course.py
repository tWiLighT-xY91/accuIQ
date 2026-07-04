from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.crud.course import (
    create_course,
    get_course,
    get_courses,
)

from app.schemas.course import (
    CourseCreate,
    CourseRead,
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)
        
@router.post(
    "/",
    response_model=CourseRead,
)
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
):
    return create_course(
        db,
        course,
    )

@router.get(
    "/",
    response_model=list[CourseRead],
)
def read_courses(
    db: Session = Depends(get_db),
):
    return get_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseRead,
)
def read_course(
    course_id: int,
    db: Session = Depends(get_db),
):
    return get_course(
        db,
        course_id,
    )
    
