"""
Deleting multiple subscriptions
Now that Sam has a maturing notification system, she is learning that the types of alerts she sends do not bode well for text messaging.

SMS alerts are great if the user can react that minute, but "We are 500 potholes behind" is not something that a Council Member can jump up and fix.

She decides to remove all SMS subscribers from the streets_critical topic, but keep all email subscriptions.

She created the boto3 SNS client in the sns variable, and the streets_critical topic ARN is in the str_critical_arn variable.

In this exercise, you will help Sam remove all SMS subscribers and make this an email only alerting system.

Instructions
100 XP
_ List subscriptions for 'streets_critical' topic.
_ For each subscription, if the protocol is 'sms', unsubscribe.
_ List subscriptions for 'streets_critical' topic in one line.
_ Print the subscriptions

"""
# List subscriptions for streets_critical topic.
response = sns.list_subscriptions_by_topic(
    TopicArn=str_critical_arn)

# For each subscription, if the protocol is SMS, unsubscribe
for sub in response['Subscriptions']:
    if sub['Protocol'] == 'sms':
        sns.unsubscribe(SubscriptionArn=sub['SubscriptionArn'])

# List subscriptions for streets_critical topic in one line
subs = sns.list_subscriptions_by_topic(
    TopicArn=str_critical_arn)['Subscriptions']

# Print the subscriptions
print(subs)
