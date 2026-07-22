from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.decision import extract_document_text
from app.services.processing.extractor import extract_candidates

from app.ai.structurer import structure_question


def main():

    db = SessionLocal()

    try:

        document_id = int(input("Document ID: "))

        document = get_document(
            db,
            document_id,
        )

        if document is None:
            print("Document not found.")
            return

        print(f"\nDocument ID: {document.id}")

        print("\nExtracting document text...")

        text = extract_document_text(document.storage_uri)

        print(f"Extracted {len(text)} characters.")

        print("\nRunning extractor...")

        candidates = extract_candidates(text)

        if not candidates:

            print("No questions extracted.")

            return

        print(f"Extracted {len(candidates)} candidates.")

        # Only test the first question for now
        for i, candidate in enumerate(candidates, start=1):
            print("\n")
            print("=" * 70)
            print("RAW QUESTION")
            print("=" * 70)

            print(candidate.raw_text)
            print("\nSending to Qwen...")
            try:

                structured = structure_question(candidate.raw_text)

                print(structured)
                print("\n")
                print("=" * 70)
                print("STRUCTURED OUTPUT")
                print("=" * 70)

            except Exception as e:

                print(f"\n❌ Candidate {i} failed")

                print(e)

                continue
    finally:

        db.close()


if __name__ == "__main__":
    main()
