import asyncio

from fastapi import UploadFile

from app.services.upload.uploader import upload_document


async def main():

    with open(
        "sample.pdf",
        "rb",
    ) as f:

        upload = UploadFile(
            filename="sample.pdf",
            file=f,
        )
        print(upload.filename)
        print(upload.content_type)
        storage_uri = await upload_document(upload)

        print(storage_uri)


asyncio.run(main())