
import boto3
session = boto3.Session(
    #aws_access_key_id="AKIA6IY36EY3CRJ5PQFI",
    #aws_secret_access_key="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",
    region_name="US East (N. Virginia) us-east-1",
)
import os

#os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA6IY36EY3CRJ5PQFI'
#os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.client('s3', region_name=region)

bucket_name = 'mybucketswetha123'

try:
    # Create the S3 bucket
    response = s3_client.list_buckets()
    for bucket in response["Buckets"]:
     print(bucket["Name"])

except ClientError as e:
    print(f'Error creating bucket: {e}')
    import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.resource('s3', region_name=region)

bucket_name = 'swetha124578'

try:
    # Read the S3 bucket

# Retrieve the list of existing buckets
    for bucket in s3_client.buckets.all():
      print(bucket.name)

except ClientError as e:
    print(f'Error creating bucket: {e}')

