"""
Generate HTML table from Pandas
Residents often complain that they don't know the full range of services offered through the Get It Done application.

In an effort to streamline the communication between the City government and the public, the City Council asked Sam to generate a table of all the services in the Get It Done system.

The system is dynamic and grows on a weekly basis, adding additional services. Sam didn't want to waste time updating the file manually, and felt like she can automate the process.

She loaded the DataFrame of available services into the services_df variable:

services_df dataframe

Instructions
100 XP
- Generate an HTML table with no border and only the 'service_name' and 'link' columns.
- Generate an HTML table with borders and all columns.
- Make sure to set all URLs to be clickable.

"""
# Generate an HTML table with no border and selected columns
services_df.to_html('./services_no_border.html',
           # Keep specific columns only
           columns=['service_name', 'link'],
           # Set border
           border=0)

# Generate an html table with border and all columns.
services_df.to_html('./services_border_all_columns.html', 
           border=1)
