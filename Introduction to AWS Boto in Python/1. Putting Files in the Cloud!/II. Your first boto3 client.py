"""

\  Your first boto3 client  /

Sam wants to cast off the shackles of only being able to use her computer for storage and compute. She is learning how to use the awesome power of the cloud 
to create data pipelines and automatically generate reports.

Before she can do all that, she needs to create her first boto3 client and check out what buckets already exist in S3.

Her AWS key and AWS secret key have been stored in AWS_KEY_ID and AWS_SECRET respectively.
In this exercise, you will help Sam by creating your first boto3 client to AWS!

Instructions
100 XP
- Generate a boto3 client for interacting with s3.
- Specify 'us-east-1' for the region_name.
- Use AWS_KEY_ID and AWS_SECRET to set up the credentials.
- Print the buckets.

"""
# Generate the boto3 client for interacting with S3
s3 = boto3.client('s3', region_name='us-east-1', 
                        # Set up AWS credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
# List the buckets
buckets = s3.list_buckets()

# Print the buckets
print(buckets)
