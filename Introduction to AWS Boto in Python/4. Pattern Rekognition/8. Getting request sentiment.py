"""
Getting request sentiment
After successfully translating Get It Done cases for the Streets Director, he asked for one more thing. He really wants to understand how people in the City feel about his department's work. She believes she can answer that question via sentiment analysis of Get It Done requests. She has already loaded the CSV into the dumping_df variable and subset it to the following columns:

Get It Done requests in many languages

In this exercise, you will help Sam better understand the moods of the voices of the people that submit Get It Done cases, and whether they are coming into the interaction with the City in a positive mood or a negative one.

Instructions
100 XP
Detect the sentiment of 'public_description' for every row.
Store the result in the 'sentiment' column.

"""
for index, row in dumping_df.iterrows():
  	# Get the translated_desc into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
      	# Get the detect_sentiment response
        response = comprehend.detect_sentiment(
          Text=description, 
          LanguageCode='en')
        # Get the sentiment key value into sentiment column
        dumping_df.loc[index, 'sentiment'] = response['Sentiment']
# Preview the dataframe
dumping_df.head()
'''
service_request_id original_lang                                                                                              public_description sentiment
0  93494               es            There is a lot of trash                                                                     NEGATIVE
1  101502              en            Couch, 4 chairs, mattress, carpet padding. this is a on going problem                       NEGATIVE
2  101520              NaN           NaN                                                                                         NEUTRAL 
3  101576              en            On the South Side of Paradise Valley Road near the intersection with Jester St. 
                                      Stuff in trash bags, rolling suitcases, and shopping carts. I suspect possessions
                                      of folk camping in the canyon.                                                             MIXED   
4  101616              es            The residents keep throwing stuff away'''
