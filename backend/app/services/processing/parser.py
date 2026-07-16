import fitz


def extract_text(
    file_path: str,
) -> str:

    document = fitz.open(file_path)

    text = []

    for page in document:

        text.append(
            page.get_text()
        )

    document.close()

    return "\n".join(text)