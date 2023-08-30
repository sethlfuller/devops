import os
import sys
import constants
import boto3
import requests
import logging

boto3.set_stream_logger('', logging.DEBUG)

OBJECT_NAME_TO_UPLOAD = sys.argv[1]

s3_client = boto3.client(
    's3',
    aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
)

#Generate the presigned URL
response = s3_client.generate_presigned_post(
    Bucket = sys.argv[2],
    Key = OBJECT_NAME_TO_UPLOAD,
    ExpiresIn = 10 
)

#Upload file to S3 using presigned URL
files = { 'file': open(OBJECT_NAME_TO_UPLOAD, 'rb')}
r = requests.post(response['url'], data=response['fields'], files=files)
print(r.status_code)