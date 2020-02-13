# Python Program to upload your file and list the existing S3 buckets 

First, The access key and the secret key are recieved from the user as inputs

The command  "getpass.getpass"  is used to mask the Keys 

If the secret key and access key are correct the file upload is successful, provided the file is present in the specified directory and, the buckets present in the aws account are listed

If the File is not present then the code throws an "File not found " error

If the credentials were incorrect then the code throws an "No Credential" error 

but in both cases the buckets present in the aws account are listed   s