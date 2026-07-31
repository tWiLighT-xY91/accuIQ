from sqlalchemy.orm import Session

from app.crud.question import create_question, get_question_by_hash
from app.crud.occurrence import create_occurrence

from app.schemas.question import QuestionCreate

from app.schemas.occurrence import OccurrenceCreate

from app.services.processing.decision import extract_document_text
from app.services.processing.extractor import extract_candidates
from app.services.processing.metadata import extract_document_metadata

from app.services.processing.normalizer import (
    generate_question_hash,
)

from app.ai.structurer import structure_question


def process_document_questions(
    db: Session,
    document,
):

    print("Extracting document text...")

    text = extract_document_text(document.storage_uri)
    
    metadata = extract_document_metadata(text)

    print("Extracting question candidates...")

    candidates = extract_candidates(text)

    print(f"Candidates found: {len(candidates)}")

    inserted_questions = 0
    inserted_occurrences = 0

    for candidate in candidates:

        print("\nProcessing question...")

        structured = structure_question(candidate.raw_text)

        question_hash = generate_question_hash(structured.question_text)

        question_create = QuestionCreate(
            question_text=structured.question_text,
            normalized_hash=question_hash,
        )

        existing = get_question_by_hash(db, question_hash)

        if existing:
            question = existing

        else:
            question = create_question(
                db,
                question_create,
            )

        occurrence_create = OccurrenceCreate(
            question_id=question.id,
            document_id=document.id,
            question_number=structured.question_number,
            page_number=candidate.page,
            marks=structured.marks or 0,
        )

        create_occurrence(
            db,
            occurrence_create,
        )

        inserted_questions += 1
        inserted_occurrences += 1

    return {
        "questions": inserted_questions,
        "occurrences": inserted_occurrences,
    }
