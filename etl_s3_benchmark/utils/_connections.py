import boto3
from decouple import config
from ..config import S3_ENDPOINT, S3_REGION, BUCKET_NAME


def get_s3_client():
    session = boto3.Session()
    client = session.client(
        "s3",
        region_name=S3_REGION,
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=config("GCP_ACCESS_KEY_ID"),  # GCS endpoint
        aws_secret_access_key=config("GCP_SECRET_ACCESS_KEY"),
    )

    return client
