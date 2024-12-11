import boto3
from decouple import config
from .config import S3_ENDPOINT, S3_REGION, BUCKET_NAME

# NOTE. Parse cs.AI 2024 PDFs
# NOTE. Get from the PDF:
#   - num_pages
#   - num_references
#   - parse references -> In cas reference doesn't exist in DB fetch it in metadata.json


def list_objects():
    # Create a session without credentials for public access
    session = boto3.Session()
    client = session.client(
        "s3",
        region_name=S3_REGION,
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=config("GCP_ACCESS_KEY_ID"),  # GCS endpoint
        aws_secret_access_key=config("GCP_SECRET_ACCESS_KEY"),
    )

    # List objects in the public bucket
    response = client.list_objects_v2(Bucket=BUCKET_NAME)
    print(response)
