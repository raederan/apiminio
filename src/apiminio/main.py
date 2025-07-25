"""Entrypoint of apiminio."""

import os

from fastapi import FastAPI, HTTPException
from minio import Minio
from minio.error import S3Error
from pydantic import BaseModel

# MinIO client setup using environment variables
MINIO = Minio(
    endpoint=os.getenv("MINIO_ENDPOINT", "minio:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
    secure=False,
)

apiminio = FastAPI(description="apiminio")


@apiminio.get("/", tags=["apiminio"])
def read_root() -> dict:
    """Root endpoint that returns a greeting message for apiminio."""
    return {"message": "yo apiminio!"}


class BucketRequest(BaseModel):
    bucket_name: str


@apiminio.get("/bucketcheck", tags=["apiminio bucket opertations"])
def check_bucket(bucket_name: str) -> dict:
    """
    Check if a specific bucket exists in MinIO S3.
    Receives a query parameter 'bucket_name'.
    Returns a message indicating whether the bucket exists.
    """
    try:
        if MINIO.bucket_exists(bucket_name):
            return {"message": f"Bucket '{bucket_name}' exists."}
        else:
            return {"message": f"Bucket '{bucket_name}' does not exist."}
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@apiminio.get("/buckets", tags=["apiminio bucket opertations"])
def list_buckets() -> dict:
    """
    List all buckets in MinIO S3.
    Returns a list of bucket names.
    """
    try:
        buckets = MINIO.list_buckets()
        if buckets is None:
            return {"buckets": []}
        else:
            bucket_names = [bucket.name for bucket in buckets]
            return {"buckets": bucket_names}
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@apiminio.post("/bucket", tags=["apiminio bucket opertations"])
def create_bucket(request: BucketRequest) -> dict:
    """
    Create a new bucket in MinIO S3.
    Receives a JSON payload with 'bucket_name'.
    Returns a success message or error if the bucket exists or creation fails.
    """
    bucket_name = request.bucket_name
    try:
        if not MINIO.bucket_exists(bucket_name):
            MINIO.make_bucket(bucket_name)
            return {"message": f"Bucket '{bucket_name}' created successfully."}
        else:
            # TODO: maybe change response code when bucket already exists
            return {"message": f"Bucket '{bucket_name}' already exists."}
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@apiminio.delete("/bucket", tags=["apiminio bucket opertations"])
def delete_bucket(request: BucketRequest) -> dict:
    """
    Delete a bucket in MinIO S3.
    Receives a JSON payload with 'bucket_name'.
    Returns a success message or error if deletion fails.
    """
    bucket_name = request.bucket_name
    try:
        if MINIO.bucket_exists(bucket_name):
            MINIO.remove_bucket(bucket_name)
            return {"message": f"Bucket '{bucket_name}' deleted successfully."}
        else:
            # TODO: maybe change response code when bucket does not exists
            return {"message": f"Bucket '{bucket_name}' does not exist."}
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
