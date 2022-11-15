"""
Making multiple files public
Transparency is important to City Council. They want to empower residents to analyze Get It Done requests and how they get prioritized.

They asked Sam to make all previous Get It Done aggregated reports since the beginning of 2019 public as well.
Sam has initialized the boto3 S3 client and assigned it to the s3 variable.

In this exercise, you will help Sam open up the data by setting the ACL of every object in the gid-staging bucket to public-read, opening up the objects to the world!

Instructions
100 XP
- List the objects in 'gid-staging' bucket starting with '2019/final_'.
- For each file in the response, give it an ACL of 'public-read'.
- Print the Public Object URL of each object.

"""
# List only objects that start with '2019/final_'
response = s3.list_objects(
    Bucket='gid-staging', Prefix='2019/final_')

# Iterate over the objects
for obj in response['Contents']:

    # Give each object ACL of public-read
    s3.put_object_acl(Bucket='gid-staging', 
                      Key=obj['Key'], 
                      ACL='public-read')
    
    # Print the Public Object URL for each object
    print("https://{}.s3.amazonaws.com/{}".format( 'gid-staging', obj['Key']))
