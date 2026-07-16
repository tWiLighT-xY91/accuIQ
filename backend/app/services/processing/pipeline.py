from app.services.processing.decision import extract_document_text


def process_document(
    document,
):

    text = extract_document_text(
        document.storage_uri
    )

    print(text[:500])