"""

\  Multiple clients  /

Sam knows that she will often have to work with more than one service at once. She wants to practice creating two separate clients for two different services in boto3.

When she is building her workflows, she will make multiple Amazon Web Services interact with each other, with a script executed on her computer.

Her AWS key id and AWS secret have been stored in AWS_KEY_ID and AWS_SECRET respectively.

'''You will help Sam initialize a boto3 client for S3, and another client for SNS.'''

She will use the S3 client to list the buckets in S3. She will use the SNS client to list topics she can publish to (you will learn about SNS topics in Chapter 3).

Instructions
100 XP
- Generate the boto3 clients for interacting with S3 and SNS.
- Specify 'us-east-1' for the region_name for both clients.
- Use AWS_KEY_ID and AWS_SECRET to set up the credentials.
- List and print the SNS topics.

"""
# Generate the boto3 client for interacting with S3 and SNS
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# List S3 buckets and SNS topics
buckets = s3.list_buckets()
topics = sns.list_topics()

# Print out the list of SNS topics
print(topics)
