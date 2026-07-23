from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.ingestion import (
    process_document_questions,
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


        if not document:
            print("Document not found")
            return


        print(
            f"\nProcessing Document {document.id}"
        )


        result = process_document_questions(
            db,
            document,
        )


        print("\n===================")
        print("INGESTION COMPLETE")
        print("===================")

        print(result)



    finally:
        db.close()



if __name__ == "__main__":
    main()