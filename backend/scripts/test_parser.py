from app.database.database import SessionLocal

from app.crud.document import get_document

from app.services.processing.parser import extract_text


db = SessionLocal()

document_id = int(
    input("Document ID: ")
)

document = get_document(
    db,
    document_id,
)

text = extract_text(
    document.storage_uri
)

print(text)