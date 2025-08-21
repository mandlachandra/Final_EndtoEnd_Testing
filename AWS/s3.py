#once login into AWS search for s3
#then for local means regional location or otherwise global location
#then click on create bucket and give the bucket name and region(Asia pacific(mumbai) and create bucket)
#Then open that bucket and click on upload button and click on add files then our system will open
#from there select any image or files and click on upload
#we can able to create folder also
#if we want download any image select that and go to actions then we can download that as well.


#bucket name should and end with .

#what is storage class in S3
#IN object property there will be storage class option
#edit that then we can see below
# S3 Stanard = frequently accessed data
# S3 Standard IA = In frequently access like mothnly once or twice
# S3 One Zone IA = It will be stored in only 1 Availability zone only
# S3 Glacier = desiged for long term purpose and cant able to open immediatley

# 1. What is Amazon S3?
# Amazon S3 (Simple Storage Service) is a scalable, high-speed, web-based cloud storage service used to store and
# retrieve any amount of data, at any time, from anywhere on the web.
#
# 2. What are the main features of S3?
# unlimited storage
# versioning
# lifecycle policies
# static website hosting
# event notifications
# Encryption
# Access control

# 3. What is an S3 bucket?
# An S3 bucket is a container for storing objects(files/data)
# All objects must be stored inside a bucket
# Each bucket name is globally unique

# 4. What is the maximum file size you can upload to S3?
# single put upload upto 5 GB
# Multipart upload up to 5 TB

# 5. What is an S3 object?
# An object is a file and its metadata stored in an S3 bucket
# it includes:
# key
# value
# metadata
# version id

# 6.What are storage classes in S3?
# S3 Standard
# S3 Intelligent-Tiering
# S3 Standard-IA
# S3 One Zone=IA
# S3 Glacier
# S3 Glacier Deep Archive
# S3 Reduced Redundancy
#
# 7. What is versioning in S3?
# S3 Versioning keeps multiple variants of an object in the same bucket.
# it helps with recovery from accidental deletes or overwrites

# 8. What happens when you delete a versioned object in S3?
# S3 adds a delete marker making the object appear deleted. older versions still exists and can be restored

# 9. How is data secured in S3?
# At rest : Server side encryption(SSE-S3,SSE-KMS,SSE-C)
# In transit : SSL/TLS
# Access control via IAM policies , bucket policies and ACLs
#
# 10. What is a pre-signed URL?
# A time limited url that allows access to a private object in S3 without making the object public

# 11. How can you host a static website using S3?
# Enable static website hosting
# upload HTML/CSS/JS files
# Set index and error documents
# Make the bucket public or use CloudFront

# 12. How is data consistency maintained in S3?
# S3 provides strong read-after-write consistency for PUT and DELETE operations in all AWS regions

# 13.What is S3 Lifecycle configuration?
# Rules to automatically transition or delete objects based on time
# (eg: archive to Glacier after 30 days delete after 365 days)

# 14. What is S3 Transfer Acceleration?
# Uses CloudFront edge locations to accelerate uploads to s3 over long distances

# 15. What is the difference between S3 and EBS?
# s3 = object storage, access over HTTP/S , scalable serverless
# EBS = Block storage, Attached to EC2, Persistent disk for EC2

# 16. What are the different ways to access S3?
# AWS Management Console
# AWS CLI
# SDKs(python boto3,java etc)
# REST API

# 17. How do you restrict access to an S3 bucket?
# IAM Policies
# Bucket policies
# Object ACLs
# VPC endpoint policies

# 18. What is the default encryption in S3?
# SSE-S3 (AES-256) if enabled. Otherwise, data is stored unencrypted unless encryption is explicitly configured.

# 19. What is bucket policy in S3?
# A JSON-based access policy applied to a bucket that controls who can do what actions on that bucket and its objects.

# 21.What is an S3 Access Point?
# A named network endpoint that simplifies managing access to shared data in S3 buckets for different applications.

# 22. What is Multipart Upload?
# A method to upload large files in parts to s3, improving upload speed reliability

# 23.How does S3 handle file overwrite?
# S3 replaces the object if versioning is off.
# If versioning is on, a new version is (created)

# 26. Can you limit S3 access to specific IPs?
# yes using bucket policy with aws:SourceIP condition

# 27. How do you audit access to S3?
# Enable CloudTrail to log api calls
# Enable S3 Access Logs for detailed object access logging
#
# What is S3 Object Lock?
# Allows you to prevent object deletion or overwriting for a specified period

# How do you clean up old files automatically in S3?
# use lifecycle rules to transition or delete files based on age or date

# What are S3 Object Tags?
# key-value pairs attached to object. useful for
# Object-level lifecycle rules
# cost allocation
# filtering during search
