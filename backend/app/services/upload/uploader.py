from pathlib import Path

from fastapi import UploadFile

from app.services.upload.models import UploadResult
from app.services.upload.storage import save_file
from app.services.upload.validator import validate_file_type


async def upload_document(
    file: UploadFile,
) -> UploadResult:
    """
    Validate and store an uploaded document.
    Returns metadata about the stored file.
    """

    data = await file.read()

    if not validate_file_type(
        file.content_type,
    ):
        raise ValueError("Unsupported file type.")

    extension = Path(file.filename).suffix.lower()

    storage_uri = save_file(
        data,
        extension,
    )

    return UploadResult(
        storage_uri=storage_uri,
        mime_type=file.content_type or "",
        file_size=len(data),
    )