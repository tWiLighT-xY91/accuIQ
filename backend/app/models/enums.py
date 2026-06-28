from enum import Enum


class DocumentType(str, Enum):
    SYLLABUS = "SYLLABUS"
    PYQ = "PYQ"
    NOTES = "NOTES"
    REFERENCE = "REFERENCE"
    LAB = "LAB"


class DocumentStatus(str, Enum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    FAILED = "FAILED"