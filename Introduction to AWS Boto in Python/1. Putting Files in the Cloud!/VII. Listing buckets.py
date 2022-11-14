"""

Listing buckets
Sam has successfully created the buckets for her pipeline. Often, data engineers build in checks into the pipeline to make sure their previous operation succeeded. Sam wants to build in a check to make sure her buckets actually got created.

She also wants to practice listing buckets. Listing buckets will let her perform operations on multiple buckets using a for loop.

She has already created the boto3 client for S3, and assigned it to the s3 variable.

Help Sam get a list of all the buckets in her S3 account and print their names!

Instructions
100 XP
- Get the buckets from S3.
- Iterate over the bucket key from response to access the list of buckets.
- Print the name of each bucket.

"""
# Get the list_buckets response
response = s3.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in response['Buckets']:
  
  	# Print the Name for each bucket
    print(bucket['Name'])
