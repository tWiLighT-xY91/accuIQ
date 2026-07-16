from app.database.database import SessionLocal

from app.workers.processor import process_document_worker


def main():

    db = SessionLocal()

    try:

        process_document_worker(
            db=db,
            document_id=8,      # Replace with your document ID
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()