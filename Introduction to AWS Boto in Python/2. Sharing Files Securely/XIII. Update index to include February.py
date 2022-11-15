"""
Update index to include February
In the previous two exercises, Sam has:

Read the daily Get It Done request logs for February.
Combined them into a single DataFrame.
Generated a DataFrame with aggregated metrics (request counts by type)
Wrote that DataFrame to a CSV and HTML final report files.
Uploaded these files to S3.
Now, she wants these files to be accessible through the directory listing. Currently, it only shows links for January reports: Screenshot of Get It Done reports listing

She has created the boto3 S3 client and stored it in the s3 variable.

Help Sam generate a new directory listing with the February's uploaded reports and store it in a DataFrame.

Instructions
100 XP
_ List the 'gid-reports' bucket objects starting with '2019/'.
_ Convert the content of the objects list to a DataFrame.
_ Create a column 'Link' that contains Public Object URL + key.
_ Preview the DataFrame.

"""
# List the gid-reports bucket objects starting with 2019/
objects_list = s3.list_objects(Bucket='gid-reports', Prefix='2019/')

# Convert the response contents to DataFrame
objects_df = pd.DataFrame(objects_list['Contents'])

# Create a column "Link" that contains Public Object URL
base_url = "http://gid-reports.s3.amazonaws.com/"
objects_df['Link'] = base_url + objects_df['Key']

# Preview the resulting DataFrame
objects_df.head()
