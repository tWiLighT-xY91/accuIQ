import uuid
from pathlib import Path

from app.core.config import settings

UPLOAD_DIRECTORY = Path(settings.UPLOAD_DIR)

UPLOAD_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

def generate_filename(
    extension: str = ".pdf",
) -> str:
    """
    Generate a unique filename.
    """

    return f"{uuid.uuid4()}{extension}"

def save_file(
    data: bytes,
    extension: str = ".pdf",
) -> str:
    """
    Save uploaded bytes to storage.
    Returns the relative storage path.
    """

    filename = generate_filename(extension)

    destination = UPLOAD_DIRECTORY / filename

    destination.write_bytes(data)

    return str(destination)