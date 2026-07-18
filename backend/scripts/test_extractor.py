from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.decision import (
    extract_document_text,
)

from app.services.processing.extractor import (
    extract_candidates,
)


def main():

    db = SessionLocal()

    try:

        document_id = int(
            input("Document ID: ")
        )

        document = get_document(
            db,
            document_id,
        )

        if document is None:

            print("Document not found.")

            return

        text = extract_document_text(
            document.storage_uri,
        )

        candidates = extract_candidates(
            text,
        )

        print()
        print(f"Detected {len(candidates)} candidate questions.")
        print()

        for index, candidate in enumerate(
            candidates,
            start=1,
        ):

            print("=" * 70)
            print(f"Candidate {index}")
            print("=" * 70)

            print(f"Section : {candidate.section}")
            print(f"Page    : {candidate.page}")

            print("-" * 70)

            print(candidate.raw_text)

            print()

    finally:

        db.close()


if __name__ == "__main__":
    main()