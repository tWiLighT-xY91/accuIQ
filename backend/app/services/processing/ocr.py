import easyocr
from pdf2image import convert_from_path
import numpy as np
_reader = None


def get_reader():

    global _reader

    if _reader is None:

        _reader = easyocr.Reader(
            ["en"],
            gpu=True,
        )

    return _reader


def pdf_to_images(
    pdf_path: str,
):

    return convert_from_path(
        pdf_path,
        dpi=300,
        fmt = "png"
    )


def extract_page_text(image):

    reader = get_reader()

    image = np.array(image)

    result = reader.readtext(
        image,
        detail=0,
    )

    return "\n".join(result)


def run_ocr(
    pdf_path: str,
):

    pages = pdf_to_images(
        pdf_path,
    )

    extracted_pages = []

    for page in pages:

        text = extract_page_text(
            page,
        )

        extracted_pages.append(
            text,
        )

    return "\n\n".join(
        extracted_pages,
    )
