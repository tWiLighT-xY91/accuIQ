from dataclasses import dataclass


@dataclass
class QuestionCandidate:
    section: str | None
    page: int
    raw_text: str