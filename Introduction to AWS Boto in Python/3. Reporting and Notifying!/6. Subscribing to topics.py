"""
Subscribing to topics
Many department directors are already receiving critical notifications.

Now Sam is ready to start subscribing City Council members.

She knows that they can be finicky, and elected officials are not known for their attention to detail or tolerance for failure.

She is nervous, but decides to start by subscribing the friendliest Council Member she knows. She got Elena Block's email and phone number.

Sam has initialized the boto3 SNS client and stored it in the sns variable.

She has also stored the topic ARN for streets_critical in the str_critical_arn variable.

Help Sam subscribe her first Council member to the streets_critical topic!

Instructions
100 XP
_ Subscribe Elena's phone number to the 'streets_critical' topic.
_ Print the SMS subscription ARN.
_ Subscribe Elena's email to the 'streets_critical topic.
_ Print the email subscription ARN.

"""
# Subscribe Elena's phone number to streets_critical topic
resp_sms = sns.subscribe(
  TopicArn = str_critical_arn, 
  Protocol='sms', Endpoint="+16196777733")

# Print the SubscriptionArn
print(resp_sms['SubscriptionArn'])

# Subscribe Elena's email to streets_critical topic.
resp_email = sns.subscribe(
  TopicArn = str_critical_arn, 
  Protocol='email', Endpoint="eblock@sandiegocity.gov")

# Print the SubscriptionArn
print(resp_email['SubscriptionArn'])
