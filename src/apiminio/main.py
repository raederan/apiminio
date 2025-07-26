"""Entrypoint of apiminio, refactored as Apiminio class."""

import os
from io import BytesIO
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from minio import Minio  # type: ignore[import-untyped]
from minio.error import S3Error  # type: ignore[import-untyped]
from pydantic import BaseModel, SecretStr


class BucketRequest(BaseModel):
    """Request model for bucket operations."""

    bucket_name: str


class MinioConfig(BaseModel):
    """Configuration model for Minio client."""

    endpoint: str = os.getenv("MINIO_ENDPOINT", "minio:9000")
    access_key: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    secret_key: SecretStr = SecretStr(os.getenv("MINIO_SECRET_KEY", "minioadmin"))
    secure: bool = bool(int(os.getenv("MINIO_SECURE", "0")))


# Inherit FastAPI so Apiminio can be used as a drop-in replacement
class Apiminio(FastAPI):
    """
    Apiminio is a REST interface inheriting FastAPI and providing Minio functionality.
    """

    def __init__(self, config: MinioConfig) -> None:
        super().__init__(description="apiminio")
        self.minio = Minio(
            endpoint=config.endpoint,
            access_key=config.access_key,
            secret_key=config.secret_key.get_secret_value(),
            secure=config.secure,
        )
        self.register_routes()

    def register_routes(self) -> None:
        """Register all routes for the Apiminio class."""

        # Default
        tag_apiminio = "apiminio"
        self.get("/", tags=[tag_apiminio])(self.read_root)
        self.get("/healthy", tags=[tag_apiminio])(self.health_check)

        # Bucket operations
        tag_bucket_operations = "apiminio bucket operations"
        self.get("/bucketnames", tags=[tag_bucket_operations])(self.list_buckets)
        self.post("/bucket", tags=[tag_bucket_operations])(self.create_bucket)
        self.delete("/bucket", tags=[tag_bucket_operations])(self.delete_bucket)

        # File operations
        tag_file_operations = "apiminio file operations"
        self.get("/filenames", tags=[tag_file_operations])(self.list_filenames)
        self.post("/file", tags=[tag_file_operations])(self.upload_file)
        self.delete("/file", tags=[tag_file_operations])(self.delete_file)

    async def read_root(self) -> dict:
        """Root endpoint for apiminio."""
        return {"message": "yo apiminio!"}

    async def health_check(self) -> dict:
        """Health check endpoint for minio connection."""
        try:
            buckets = self.minio.list_buckets()
            if buckets is None:
                return {"alive": True}
            else:
                return {"alive": True}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
            return {"alive": False}

        # Fallback for mypy, though unreachable

    async def list_buckets(self) -> dict:
        """List all bucket names."""
        try:
            buckets = self.minio.list_buckets()
            if buckets is None:
                return {"buckets": []}
            else:
                bucket_names = [bucket.name for bucket in buckets]
                return {"buckets": bucket_names}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    async def create_bucket(self, request: BucketRequest) -> dict:
        """Create a new bucket."""
        bucket_name = request.bucket_name
        try:
            if not self.minio.bucket_exists(bucket_name):
                self.minio.make_bucket(bucket_name)
                return {"message": f"Bucket '{bucket_name}' created successfully."}
            else:
                raise HTTPException(status_code=404, detail=f"Bucket '{bucket_name}' already exists.")
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    async def delete_bucket(self, request: BucketRequest) -> dict:
        """Delete an existing bucket."""
        bucket_name = request.bucket_name
        try:
            if self.minio.bucket_exists(bucket_name):
                self.minio.remove_bucket(bucket_name)
                return {"message": f"Bucket '{bucket_name}' deleted successfully."}
            else:
                raise HTTPException(status_code=404, detail=f"Bucket '{bucket_name}' does not exist.")
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    async def list_filenames(self, bucket_name: str) -> dict:
        """List all files in a bucket."""
        try:
            if self.minio.bucket_exists(bucket_name):
                objects = self.minio.list_objects(bucket_name)
                return {"files": [obj.object_name for obj in objects]}
            else:
                raise HTTPException(status_code=404, detail=f"Bucket '{bucket_name}' does not exist.")
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    async def upload_file(self, bucket_name: str = Form(...), file: Optional[UploadFile] = None) -> dict:
        """Upload a file to a specified bucket."""
        if file is None:
            file = File(...)
        try:
            if self.minio.bucket_exists(bucket_name):
                file_bytes = await file.read()
                file_stream = BytesIO(file_bytes)
                self.minio.put_object(
                    bucket_name=bucket_name, object_name=file.filename, data=file_stream, length=len(file_bytes)
                )
                return {"filename": file.filename}
            else:
                return {"message": f"Bucket '{bucket_name}' does not exist."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    async def delete_file(self, bucket_name: str = Form(...), file_name: str = Form(...)) -> dict:
        """Delete a file from a specified bucket, checking if file exists first."""
        try:
            if not self.minio.bucket_exists(bucket_name):
                raise HTTPException(status_code=404, detail=f"Bucket '{bucket_name}' does not exist.")

            # Check if file exists in bucket
            objects = self.minio.list_objects(bucket_name, prefix=file_name, recursive=False)
            file_exists = any(obj.object_name == file_name for obj in objects)
            if not file_exists:
                raise HTTPException(
                    status_code=404, detail=f"File '{file_name}' does not exist in bucket '{bucket_name}'."
                )
            else:
                self.minio.remove_object(bucket_name, file_name)
                return {"message": f"File '{file_name}' deleted successfully from bucket '{bucket_name}'."}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e)) from e


# Instantiate Apiminio directly as you would FastAPI including a Minio configuration
apiminio = Apiminio(config=MinioConfig())
