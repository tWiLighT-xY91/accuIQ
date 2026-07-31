import re

from app.services.processing.models import QuestionCandidate

QUESTION_PATTERNS = [
    r"^Question\s+\d+",
    r"^Q\.?\s*\d+",
    r"^\d+\s*\.",
    r"^\d+\s*\)",
]

END_PATTERNS = [
    r"^Course Outcomes",
    r"^CO1\s*:",
]


def normalize_text(text: str) -> str:
    """
    Cleans parser output before question extraction.
    """

    text = text.replace("\r", "")

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    return text.strip()


def split_into_lines(text: str) -> list[str]:
    """
    Splits text into clean non-empty lines.
    """

    return [line.strip() for line in text.splitlines() if line.strip()]


def is_question_start(line: str) -> bool:
    """
    Returns True if the line looks like the beginning
    of a new question.
    """

    for pattern in QUESTION_PATTERNS:

        if re.match(
            pattern,
            line,
            flags=re.IGNORECASE,
        ):
            return True

    return False


def extract_section(line: str) -> str | None:
    """
    Detects section headers such as
    Section A
    Section B
    """

    match = re.match(
        r"Section\s+([A-Za-z])",
        line,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(1).upper()

    return None


def extract_candidates(text: str) -> list[QuestionCandidate]:

    text = normalize_text(text)

    lines = split_into_lines(text)

    candidates: list[QuestionCandidate] = []

    current_question: list[str] = []

    current_section: str | None = None

    started = False

    page = 1

    for line in lines:

        # Track sections
        section = extract_section(line)

        if section:
            current_section = section
            continue

        # Ignore everything before first question
        if not started:

            if is_question_start(line):
                started = True
            else:
                continue

        # New Question
        if is_question_start(line):

            if current_question:

                candidates.append(
                    QuestionCandidate(
                        section=current_section,
                        page=page,
                        raw_text="\n".join(current_question),
                    )
                )

                current_question = []

        current_question.append(line)

    if current_question:

        candidates.append(
            QuestionCandidate(
                section=current_section,
                page=page,
                raw_text="\n".join(current_question),
            )
        )

    return candidates
