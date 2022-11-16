"""
Detecting language
The City Council is wondering whether it's worth it to build a Spanish version of the Get It Done application. There is a large Spanish speaking constituency, but they are not sure if they will engage. Building in multi-lingual translation complicates the system and needs to be justified.

They ask Sam to figure out how many people are posting requests in Spanish.

She has already loaded the CSV into the dumping_df variable and subset it to the following columns:

Get It Done requests in many languages

Help Sam quantify the demand for a Spanish version of the Get It Done application. Figure out how many requesters use Spanish and print the final result!

Instructions
100 XP
For each row in the DataFrame, detect the dominant language.
Assign the first selected language to the 'lang' column.
Count the total number of posts in Spanish.

"""
# For each dataframe row
for index, row in dumping_df.iterrows():
    # Get the public description field
    description =dumping_df.loc[index, 'public_description']
    if description != '':
        # Detect language in the field content
        resp = comprehend.detect_dominant_language(Text=description)
        # Assign the top choice language to the lang column.
        dumping_df.loc[index, 'lang'] = resp['Languages'][0]['LanguageCode']
        
# Count the total number of spanish posts
spanish_post_ct = len(dumping_df[dumping_df.lang == 'es'])
# Print the result
print("{} posts in Spanish".format(spanish_post_ct))
'''
9 posts in Spanish
'''
