import re

from app.schemas.metadata import DocumentMetadata


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------

def extract_document_metadata(
    text: str,
) -> DocumentMetadata:
    """
    Extract metadata from the document text.

    Strategy:
        1. Extract deterministic metadata using regex.
        2. If required fields are still missing, fall back to the LLM.
        3. Merge both results.
    """

    regex_metadata = _extract_with_regex(text)

    if regex_metadata.exam_year is not None:
        return regex_metadata

    llm_metadata = _extract_with_llm(text)

    return _merge_metadata(
        regex_metadata,
        llm_metadata,
    )


# ---------------------------------------------------------------------
# Regex Extraction
# ---------------------------------------------------------------------

def _extract_with_regex(
    text: str,
) -> DocumentMetadata:
    """
    Extract metadata using deterministic regex rules.
    """

    metadata = DocumentMetadata()

    # ---------------------------------------------------------
    # Exam Year
    # Matches:
    #
    # 2024-25
    # 2024–25
    # 2024/25
    # 2024
    # ---------------------------------------------------------

    year_patterns = [

        r"\b(20\d{2})\s*[-–/]\s*\d{2}\b",

        r"\b(20\d{2})\b",
    ]

    for pattern in year_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:

            metadata.exam_year = int(
                match.group(1)
            )

            break

    # ---------------------------------------------------------
    # Course Code
    #
    # Matches:
    #
    # Course Code : MC302
    # COURSE CODE- CS210
    # Course Code MC301
    # ---------------------------------------------------------

    course_match = re.search(

        r"course\s*code\s*[:\-]?\s*([A-Za-z0-9\-]+)",

        text,

        re.IGNORECASE,

    )

    if course_match:

        metadata.course_code = (
            course_match.group(1)
            .strip()
            .upper()
        )

    return metadata


# ---------------------------------------------------------------------
# LLM Extraction
# ---------------------------------------------------------------------

def _extract_with_llm(
    text: str,
) -> DocumentMetadata:
    """
    Placeholder for future Qwen metadata extraction.

    Sprint 4 uses regex only.

    Sprint 5 (or later) will upgrade this function to use the
    existing AI client and metadata prompt.
    """

    return DocumentMetadata()


# ---------------------------------------------------------------------
# Merge Strategy
# ---------------------------------------------------------------------

def _merge_metadata(
    regex_metadata: DocumentMetadata,
    llm_metadata: DocumentMetadata,
) -> DocumentMetadata:
    """
    Prefer regex values.

    Use LLM values only if regex couldn't determine them.
    """

    return DocumentMetadata(

        exam_year=(
            regex_metadata.exam_year
            or llm_metadata.exam_year
        ),

        course_code=(
            regex_metadata.course_code
            or llm_metadata.course_code
        ),

        course_name=(
            regex_metadata.course_name
            or llm_metadata.course_name
        ),

        semester=(
            regex_metadata.semester
            or llm_metadata.semester
        ),

        exam_type=(
            regex_metadata.exam_type
            or llm_metadata.exam_type
        ),

        institution=(
            regex_metadata.institution
            or llm_metadata.institution
        ),

    )


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

