from app.core.config import settings


def validate_file_type(content_type: str) -> bool:
    """
    Check whether the uploaded file type is allowed.
    """

    return content_type in settings.ALLOWED_FILE_TYPES


def validate_file_size(file_size: int) -> bool:
    """
    Check whether the uploaded file size is within limits.
    """

    max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024

    return file_size <= max_size