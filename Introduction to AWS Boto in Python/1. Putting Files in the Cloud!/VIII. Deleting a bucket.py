"""

Deleting a bucket
Sam is feeling more and more confident in her AWS and S3 skills. After playing around for a bit, she decides that the gim-test bucket no longer fits her pipeline and wants to delete it. It's starting to feel like dead weight, and Sam doesn't want it littering her beautiful bucket list.

She has already created the boto3 client for S3, and assigned it to the s3 variable.

Help Sam do some clean up, and delete the gim-test bucket.

Instructions
100 XP
- Delete the 'gim-test' bucket.
- Get the list of buckets from S3.
- Print each 'Buckets' 'Name'.

"""
# Delete the gim-test bucket
s3.delete_bucket(Bucket='gim-test')

# Get the list_buckets response
response = s3.list_buckets()

# Print each Buckets Name
for bucket in response['Buckets']:
    print(bucket['name'])
