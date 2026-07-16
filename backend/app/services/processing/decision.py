from app.services.processing.parser import extract_text
from app.services.processing.ocr import run_ocr

def extract_document_text(
    file_path: str,
):

    text = extract_text(file_path)

    if len(text.strip()) > 100:

        return text

    return run_ocr(file_path)