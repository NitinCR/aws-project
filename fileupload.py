import logging
import boto3
from botocore.exceptions import ClientError
a = input("enter the file Name")
b = input("enter the object Name")
c = input("choose your desired bucket")
def upload_file(file_name, bucket, object_nme=None):
    if object_nme is None:
        object_nme = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_nme)
    except ClientError as e:
        logging.error(e)
        return false 
    return True
upload_file(file_name = a,bucket = c,object_nme = b)

s3 = boto3.client('s3')
with open(a, "rb") as f:
    s3.upload_fileobj(f, c, b)



s3.upload_file(
    a, c, b,
    ExtraArgs={'ACL': 'public-read'}
)

   


