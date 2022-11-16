"""
Different protocols per topic level
Now that Sam has created the critical and extreme topics, she needs to subscribe the staff from her contact list into these topics.

Sam decided that the people subscribed to 'critical' topics will only receive emails. On the other hand, people subscribed to 'extreme' topics will receive SMS - because those are pretty urgent.

She has already created the boto3 SNS client in the sns variable.

Help Sam subscribe the users in the contacts DataFrame to email or SMS notifications based on their department. This will help get the right alerts to the right people, making the City of San Diego run better and faster!

Instructions
100 XP
_ Get the topic name by using the 'Department' field in the contacts DataFrame.
_ Use the topic name to create the critical and extreme TopicArns for a user's department.
_ Subscribe the user's email address to the critical topic.
_ Subscribe the user's phone number to the extreme topic.

"""
for index, user_row in contacts.iterrows():
  # Get topic names for the users's dept
  critical_tname = '{}_critical'.format(user_row['Department'])
  extreme_tname = '{}_extreme'.format(user_row['Department'])
  
  # Get or create the TopicArns for a user's department.
  critical_arn = sns.create_topic(Name=critical_tname)['TopicArn']
  extreme_arn = sns.create_topic(Name=extreme_tname)['TopicArn']
  
  # Subscribe each users email to the critical Topic
  sns.subscribe(TopicArn = critical_arn, 
                Protocol='email', Endpoint=user_row['Email'])
  # Subscribe each users phone number for the extreme Topic
  sns.subscribe(TopicArn = extreme_arn, 
                Protocol='sms', Endpoint=str(user_row['Phone']))
