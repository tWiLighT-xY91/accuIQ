"""from pathlib import Path

from app.services.upload.storage import save_file


sample_data = b"Hello AccuIQ"

storage_uri = save_file(sample_data)

print("Saved to:")

print(storage_uri)

print()

print("Exists:")

print(Path(storage_uri).exists())

"""
from app.services.upload.validator import (
    validate_file_type,
    validate_file_size,
)

print(validate_file_type("application/pdf"))

print(validate_file_type("image/png"))

print(validate_file_size(1024))

print(validate_file_size(100000000))