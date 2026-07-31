from app.services.processing.decision import extract_document_text
from app.services.processing.metadata import extract_document_metadata


FILE_PATH = "test_files/CSC Odd Sem End-term 2023-24.pdf"


def main():

    print("Extracting text...")

    text = extract_document_text(FILE_PATH)

    print("Extracting metadata...")

    metadata = extract_document_metadata(text)

    print("\nMetadata Extracted")
    print("=" * 40)

    print(metadata.model_dump())


if __name__ == "__main__":
    main()