from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.ocr import run_ocr


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

        print("\nRunning OCR...\n")

        text = run_ocr(
            document.storage_uri,
        )

        print("=" * 80)
        print("OCR OUTPUT")
        print("=" * 80)

        if not text.strip():

            print("No text detected.")

            return

        print(text)

        print()
        print("=" * 80)
        print(f"Extracted {len(text)} characters.")
        print("=" * 80)

    finally:

        db.close()


if __name__ == "__main__":
    main()
