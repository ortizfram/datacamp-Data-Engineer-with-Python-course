"""
Creating multiple subscriptions
After the successful pilot with Councilwoman Elena Block, other City Council members have been asking to be signed up for alerts too.

Sam decides that she should manage subscribers in a CSV file, otherwise she would lose track of who needs to be subscribed to what.

She creates a CSV named contacts and decides to subscribe everyone in the CSV to the streets_critical topic.

She has created the boto3 SNS client in the sns variable, and the streets_critical topic ARN is in the str_critical_arn variable.

Sam is going from being a social pariah to being courted by multiple council offices.

Help her solidify her position as master of all information by adding all the users in her CSV to the streets_critical topic!

Instructions
100 XP
_ For each element in the Email column of contacts, create a subscription to the 'streets_critical' Topic.
_ List subscriptions for the 'streets_critical' Topic and convert them to a DataFrame.
_ Preview the DataFrame.

"""
# For each email in contacts, create subscription to street_critical
for email in contacts['Email']:
  sns.subscribe(TopicArn = str_critical_arn,
                # Set channel and recipient 
                Protocol = 'email', #channel
                Endpoint = email)   # recipient

# List subscriptions for streets_critical topic, convert to DataFrame
response = sns.list_subscriptions_by_topic(
  TopicArn = str_critical_arn)
subs = pd.DataFrame(response['Subscriptions'])

# Preview the DataFrame
subs.head()
