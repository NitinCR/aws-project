import boto3
import getpass
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = getpass.getpass("Enter your access key : ")
SECRET_KEY = getpass.getpass("Enter your secret key : ")


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
        return True
    except FileNotFoundError:
        print("The file was not found")
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')


uploaded = upload_to_aws('fileupload.py', 'aws-test12', 'aws')
