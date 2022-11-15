"""
Upload the new index
Sam is almost done! In the last exercise, she generated a new directory listing, storing it in the objects_df variable:

Screenshot of objects_df

Sam has created the boto3 S3 client in the s3 variable. objects_df is populated with the new directory listing from the previous exercise.

The next step is to write objects_df to an HTML file, and upload it to S3 replacing the current 'index.html' file.

Help Sam update the directory listing, letting the public access reports for February as well as January!

Instructions
100 XP
_ Write objects_df to an HTML file 'report_listing.html' with clickable links.
_ The HTML file should only contain 'Link', 'LastModified', and 'Size' columns.
_ Overwrite the 'index.html' on S3 by uploading the new version of the file.

"""
# Write objects_df to an HTML file
objects_df.to_html('report_listing.html',
    # Set clickable links
    render_links=True,
	# Isolate the columns
    columns=['Link', 'LastModified', 'Size'])

# Overwrite index.html key by uploading the new file
s3.upload_file(
  Filename='./report_listing.html', Key='index.html', 
  Bucket='gid-reports',
  ExtraArgs = {
    'ContentType': 'text/html', 
    'ACL': 'public-read'
  })
