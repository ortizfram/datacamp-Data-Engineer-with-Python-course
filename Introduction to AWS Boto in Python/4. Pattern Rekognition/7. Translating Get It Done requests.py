"""
Translating Get It Done requests
Often, Get It Done requests come in with multiple languages in the description. This is a challenge for many City teams. In order to review the requests, many city teams need to have a translator on staff, or hope they know someone who speaks the language.

The Streets director asked Sam to help. He wanted her to translate the Get It Done requests by running a job at the end of every day.

Sam decides to run the requests through the AWS translate service. She has already loaded the CSV into the dumping_df variable and subset it to the following columns:

Get It Done requests in many languages

Help Sam translate the requests to Spanish by running them through the AWS translate service!

Instructions
100 XP
For each row in the DataFrame, translate it to English.
Store the original language in the original_lang column.
Store the new translation in the translated_desc column.

"""
for index, row in dumping_df.iterrows():
  	# Get the public_description into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
      	# Translate the public description
        resp = translate.translate_text(
            Text=description, 
            SourceLanguageCode='auto', TargetLanguageCode='en')
        # Store original language in original_lang column
        dumping_df.loc[index, 'original_lang'] = resp['SourceLanguageCode']
        # Store the translation in the translated_desc column
        dumping_df.loc[index, 'translated_desc'] = resp['TranslatedText'] # output
# Preview the resulting DataFrame
dumping_df = dumping_df[['service_request_id', 'original_lang', 'translated_desc']]
dumping_df.head()
'''
service_request_id original_lang                                    translated_desc
0               93494            es             The residents keep throwing stuff away
1              101502            en  Couch, 4 chairs, mattress, carpet padding. thi...
2              101520           NaN                                                NaN
3              101576            en  On the South Side of Paradise Valley Road near...
4              101616            es                    There is a fridge on the street
'''
