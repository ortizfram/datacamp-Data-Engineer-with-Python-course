"""
Creating multiple topics
Sam suddenly became a black sheep because she is responsible for an onslaught of text messages and notifications to department directors.

No one will go to lunch with her anymore!

To fix this, she decided to create a general topic per department for routine notifications, and a critical topic for urgent notifications.

Managers will subscribe only to critical notifications, while supervisors can monitor general notifications.

For example, the streets department would have 'streets_general' and 'streets_critical' as topics.

She has initialized the SNS client and stored it in the sns variable.

Help Sam create a tiered topic structure… and have friends again!

Instructions
100 XP
_ For every department, create a general topic.
_ For every department, create a critical topic.
_ Print all the topics created in SNS

"""
# Create list of departments
departments = ['trash', 'streets', 'water']

for dept in departments:
  	# For every department, create a general topic
    sns.create_topic(Name="{}_general".format(dept))
    
    # For every department, create a critical topic
    sns.create_topic(Name="{}_critical".format(dept))

# Print all the topics in SNS
response = sns.list_topics()
print(response['Topics'])
