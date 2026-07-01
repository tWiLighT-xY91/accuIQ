from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
)


def create_course(
    db: Session,
    course: CourseCreate,
) -> Course:

    db_course = Course(**course.model_dump())

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def get_course(
    db: Session,
    course_id: int,
) -> Course | None:

    statement = select(Course).where(Course.id == course_id)

    return db.scalar(statement)


def get_courses(
    db: Session,
):

    statement = (
        select(Course)
        .order_by(Course.course_name)
    )

    return list(
        db.scalars(statement)
    )
    
def update_course(
    db: Session,
    db_course: Course,
    updates: CourseUpdate,
) -> Course:

    update_data = updates.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_course,
            key,
            value,
        )

    db.commit()
    db.refresh(db_course)

    return db_course

def delete_course(
    db: Session,
    db_course: Course,
):

    db.delete(db_course)
    db.commit()
    
