"""
Opening a private file
The City Council wants to see the bigger trend and have asked Sam to total up all the requests since the beginning of 2019. In order to do this, Sam has to read daily CSVs from the 'gid-requests' bucket and concatenate them. However, the gid-requests files are private. She has access to them via her key, but the world cannot access them.

In this exercise, you will help Sam see the bigger picture by reading these private files into pandas and concatenating them into one DataFrame!

She has already initialized the boto3 S3 client and assigned it to the s3 variable. She has listed all the objects in gid-requests in the response variable.

Instructions
100 XP
- For each file in response, load the object from S3.
- Load the object's StreamingBody into pandas, and append to df_list.
- Concatenate all the DataFrames with pandas.
- Preview the resulting DataFrame

"""
df_list =  [ ] 

for file in response['Contents']:
    # For each file in response load the object from S3
    obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
    # Load the object's StreamingBody with pandas
    obj_df = pd.read_csv(obj['Body'])
    # Append the resulting DataFrame to list
    df_list.append(obj_df)

# Concat all the DataFrames with pandas
df = pd.concat(df_list)

# Preview the resulting DataFrame
df.head()

'''        service_name  request_count
        0  72 Hour Violation              8
        1   Graffiti Removal              2
        2  Missed Collection             12
        3   Street Light Out             21
        4            Pothole             33'''
