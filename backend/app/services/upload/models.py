from pydantic import BaseModel


class UploadResult(BaseModel):
    storage_uri: str
    mime_type: str
    file_size: int