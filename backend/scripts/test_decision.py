from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.decision import extract_document_text


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

        text = extract_document_text(
            document.storage_uri,
        )

        print("\n===== Extracted Text =====\n")
        print(text[:1000])

    finally:

        db.close()


if __name__ == "__main__":
    main()