from app.database.database import SessionLocal

# CRUD
from app.crud.course import *
from app.crud.document import *
from app.crud.question import *
from app.crud.occurrence import *

# Schemas
from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
)

from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
)

from app.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
)

from app.schemas.occurrence import (
    OccurrenceCreate,
    OccurrenceUpdate,
)

# Enums
from app.models.enums import (
    DocumentType,
    DocumentStatus,
)

db = SessionLocal()

try:

    print("\n========== CREATE ==========\n")

    # ---------------------------------------------------
    # COURSE
    # ---------------------------------------------------

    course = create_course(
        db,
        CourseCreate(
            course_name="Operating Systems",
            course_code="CS301",
            semester=5,
            branch="CSE",
            university="NIT Durgapur",
        ),
    )

    print(f"✓ Course Created (ID={course.id})")

    # ---------------------------------------------------
    # DOCUMENT
    # ---------------------------------------------------

    document = create_document(
        db,
        DocumentCreate(
            course_id=course.id,
            title="Operating Systems Midsem 2024",
            storage_uri="uploads/os_midsem_2024.pdf",
            mime_type="application/pdf",
            file_size=204800,
            checksum="test_checksum_001",
            document_type=DocumentType.PYQ,
            status=DocumentStatus.UPLOADED,
            exam_year=2024,
            pages=8,
        ),
    )

    print(f"✓ Document Created (ID={document.id})")

    # ---------------------------------------------------
    # QUESTION
    # ---------------------------------------------------

    question = create_question(
        db,
        QuestionCreate(
            question_text="Explain Deadlock Prevention.",
            normalized_hash="deadlock_hash",
        ),
    )

    print(f"✓ Question Created (ID={question.id})")

    # ---------------------------------------------------
    # OCCURRENCE
    # ---------------------------------------------------

    occurrence = create_occurrence(
        db,
        OccurrenceCreate(
            question_id=question.id,
            document_id=document.id,
            question_number=5,
            page_number=3,
            marks=10,
        ),
    )

    print(f"✓ Occurrence Created (ID={occurrence.id})")

    print("\n========== READ ==========\n")

    course = get_course(db, course.id)
    print("✓", course.course_name)

    document = get_document(db, document.id)
    print("✓", document.title)

    question = get_question(db, question.id)
    print("✓", question.question_text)

    occurrence = get_occurrence(db, occurrence.id)
    print("✓ Question Number:", occurrence.question_number)

    print()

    print("Courses:", len(get_courses(db)))
    print("Documents:", len(get_documents(db)))
    print("Questions:", len(get_questions(db)))
    print("Occurrences:", len(get_occurrences(db)))

    print("\n========== UPDATE ==========\n")

    course = update_course(
        db,
        course,
        CourseUpdate(
            semester=6,
        ),
    )

    print("✓ Course Semester:", course.semester)

    document = update_document(
        db,
        document,
        DocumentUpdate(
            pages=10,
        ),
    )

    print("✓ Document Pages:", document.pages)

    question = update_question(
        db,
        question,
        QuestionUpdate(
            question_text="Explain Deadlock Avoidance.",
        ),
    )

    print("✓ Question:", question.question_text)

    occurrence = update_occurrence(
        db,
        occurrence,
        OccurrenceUpdate(
            marks=15,
        ),
    )

    print("✓ Occurrence Marks:", occurrence.marks)

    print("\n========== DELETE ==========\n")

    delete_occurrence(
        db,
        occurrence,
    )

    print("✓ Occurrence Deleted")

    delete_question(
        db,
        question,
    )

    print("✓ Question Deleted")

    delete_document(
        db,
        document,
    )

    print("✓ Document Deleted")

    delete_course(
        db,
        course,
    )

    print("✓ Course Deleted")

    print("\n========== VERIFY ==========\n")

    print("Courses:", len(get_courses(db)))
    print("Documents:", len(get_documents(db)))
    print("Questions:", len(get_questions(db)))
    print("Occurrences:", len(get_occurrences(db)))

    print("\n🎉 ALL CRUD TESTS PASSED!")

except Exception as e:
    print("\n❌ TEST FAILED")
    print(e)
    raise

finally:
    db.close()
