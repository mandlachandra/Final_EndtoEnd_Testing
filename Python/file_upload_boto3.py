import boto3

s3 = boto3.client('s3')
s3.upload_file("c:/path/to/your/file.txt","your-bucket-name","uploaded-file.txt")
print("file uploaded successfully using boto3.")

