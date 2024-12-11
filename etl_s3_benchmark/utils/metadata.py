from etl_s3_benchmark.utils._connections import get_s3_client
from etl_s3_benchmark.config import BUCKET_NAME


def get_metadata():
    s3_client = get_s3_client()
    metadata_file = s3_client.get_object(
        Bucket=BUCKET_NAME, Key="metadata-v5/arxiv-metadata-oai.json"
    )

    with open("arxiv-metadata-oai.json", "w") as file:
        file.write(metadata_file["Body"].read())


get_metadata()
