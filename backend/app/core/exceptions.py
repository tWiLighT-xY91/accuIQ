class AccuIQException(Exception):
    """Base exception for the application."""


class DocumentProcessingError(AccuIQException):
    """Raised when document processing fails."""