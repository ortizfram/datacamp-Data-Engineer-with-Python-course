"""
Combine daily requests for February
It's been a month since Sam last ran the report script, and it's time for her to make a new report for February.

She wants to upload new reports for February and update the file listing, expanding on the work she completed during the last video lesson:

Directory listing screenshot

She has already created the boto3 S3 client and stored in the s3 variable. She stored the contents of her objects in request_files.

You will help Sam aggregate the requests from February by downloading files from the gid-requests bucket and concatenating them into one DataFrame!

Instructions
100 XP
_ Load each object from s3.
_ Read it into pandas and append it to df_list.
_ Concatenate all DataFrames in df_list.
_ Preview the DataFrame.

"""
df_list = [] 

# Load each object from s3
for file in request_files:
    s3_day_reqs = s3.get_object(Bucket='gid-requests', 
                                Key=file['Key'])
    # Read the DataFrame into pandas, append it to the list
    day_reqs = pd.read_csv(s3_day_reqs['Body'])
    df_list.append(day_reqs)

# Concatenate all the DataFrames in the list
all_reqs = pd.concat(df_list)

# Preview the DataFrame
all_reqs.head()
