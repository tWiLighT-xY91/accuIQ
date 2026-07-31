import hashlib
import re


def normalize_question(text: str) -> str:
    """
    Normalize question text before hashing.
    Used for duplicate detection.
    """

    text = text.lower()

    # remove extra spaces/newlines
    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    # remove special noise
    text = re.sub(
        r"[^\w\s]",
        "",
        text,
    )

    return text.strip()



def generate_question_hash(text: str) -> str:
    """
    Generates SHA256 hash for duplicate detection.
    """

    normalized = normalize_question(text)

    return hashlib.sha256(
        normalized.encode("utf-8")
    ).hexdigest()