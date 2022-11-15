"""
Deleting multiple topics
It's hard to get things done in City government without good relationships. Sam is burning bridges with the general topics she created in the last exercise.

People are shunning her because she is blowing up their phones with notifications.

She decides to get rid of the general topics per department completely, and keep only critical topics.

Sam has created the boto3 client for SNS and stored it in the sns variable.

Help Sam regain her status in the bureaucratic social hierarchy by removing any topics that do not have the word critical in them.

Instructions
100 XP
_ Get the current list of topics.
_ For every topic ARN, if it doesn't have the word 'critical' in it, delete it.
_ Print the list of remaining critical topics.

"""
# Get the current list of topics
topics = sns.list_topics()['Topics']

for topic in topics:
  # For each topic, if it is not marked critical, delete it
  if "critical" not in topic['TopicArn']:
    sns.delete_topic(TopicArn=topic['TopicArn'])
    
# Print the list of remaining critical topics
print(sns.list_topics()['Topics'])
