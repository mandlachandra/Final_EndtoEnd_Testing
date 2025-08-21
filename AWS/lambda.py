# #click on create a function ->Author from scratch or use a blueprint options
# #select any function like eg:canary function
# Function name = yt-canary
# Runtime =python3.10
# Execution role =create a new role with basic lambda permissions
# once it is run in the backend a cloudwatch logs will create in backend
# this will create with the help of create a new role with basic lambda function role
#
# Eventbridge (Cloudwatch Events) trigger
# create a new role
# Rule description = trigger for every 5 mins
#
# Rule type = Event pattern or Schedule pattern
#
# Environment variables
# key
# site= "https://www.google.com"
# expected = "Gmail"
#
# Encryption configuration
# (default)aws/lambda
# Then create a function
#
# #lambda cost
# code size
# memory used
# for any request how much memory utilized
# duation 416ms
# max memory used
# 45mb
#
# In cloudwatch log groups all logs are stored
#
# To run a code the time required in 10 secs
# if it wont run in 10 secs then we will get timeout exception
#
# To avoid Timeout exception then go to
# general configuation ->edit ->there we can give max = 15 secs
# default memory is 128 MB if you have to increase that then edit ->memory ->1024mb ->save
#

# 1. What is AWS Lambda?
# AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers
# you can pay for compute time you consume

# 2. What are the key features of AWS Lambda?
# No server management
# Auto-scaling
# pay-as-you-go
# Event driven
# Integration with aws services(eg:s3,API gateway)

# 3. What languages does Lambda support?
# Node.js
# python
# java
# go
# ruby
# c#

# 4. What is the maximum timeout limit for a Lambda function?
# 15 minutes(900 seconds) is the maximum execution time for a lambda function

# 5. What triggers can be used with Lambda?
# S3(on file upload)
# Dynamo DB
# API Gateway
# Cloudwatch Events and logs
# SQS,SNS
# EventBridge
# Cognito

# 6. How is Lambda billed?
# Number of requests
# Execution duration(ms)
# Amount of memory allocated

# 7. What is a Lambda execution role?
# Its an IAM role that grants the function permissions to access other AWS resources like S3,Dynamo DB,Cloudwatch

# 8. How do you deploy Lambda functions?
# you can deploy via
# AWS Console
# AWS CLI
# AWS SDK
# CI/CD Pipeline
# Serverless framework
#
# 9. What are Lambda Layers?
# Lambda layers allow you to share libraries or dependencies across multiple functions
# it helsp keep functions lighweight and modular
#
# 10. What is the cold start in Lambda?
# Cold start occurs when AWS initializes a new container to run yourlambda functions
# it can cause latency

# 11. How can you reduce cold starts in Lambda?
# Avoid VPC unless needed
#
# Use lightweight packages
#
# Use provisioned concurrency
#
# Keep function warm (via scheduled events)

# 12. Can a Lambda function call another Lambda?
# yes using AWS SDK (e.g:boto3 or AWS.Lambda.Invoke in Node.js), one lambda can invoke another synchronously or asynchronously


# 13. What’s the max size of the deployment package?
# Direct upload : 50 MB(Zipped)
# unzipped : 250 MB
#     Via s3 : 250 MB unzipped
#     Container image :up to 10 GB
#
# 14. What’s the max memory a Lambda function can have?
# UP TO 10 GB of memory per invocation

# 15. What are the Lambda concurrency types?
# Unreserved concurrency: Default
# Reserved concurrency: Guarantees availability
# Provisioned concurrency: Pre-warms environments to avoid cold starts

# 16. How does error handling work in Lambda?
#
# Try/Except blocks (in code)
#
# Dead Letter Queues (DLQs) for failed async invocations
#
# Retry policies (for asynchronous events)
#
# CloudWatch Logs for debugging
#
# 17. What is the difference between synchronous and asynchronous Lambda invocation?
# Answer:
#
# Synchronous: Caller waits for result (e.g., API Gateway)
#
# Asynchronous: Returns immediately; Lambda processes later (e.g., S3 event)

# 18. How do you monitor Lambda functions?
#
# CloudWatch Logs
#
# CloudWatch Metrics (invocations, errors, duration)
#
# X-Ray (for tracing)
#
# AWS CloudTrail (audit logs)

# 19. How do environment variables work in Lambda?
# Answer:
# They are key-value pairs set during configuration and accessible in code using os.environ['KEY'].

# 20. Can Lambda run inside a VPC? What are the implications?
# Answer:
# Yes. But it may cause:
#
# Longer cold starts
#
# You need to configure NAT Gateway for internet access
#
# Must set subnet and security group





