"""
Scooter dispatch
The City Council were huge fans of Sam's prediction about whether scooter was blocking a sidewalk or not. So much so, they asked her to build a notification system to dispatch crews to impound scooters from sidewalks.

With the dataset she created, Sam can dispatch crews to the case's coordinates when a request has negative sentiment.

Scooter Dataframe

In this exercise, you will help Sam implement a system that dispatches crews based on sentiment and image recognition. You will help Sam pair human and machine for effective City management!

Instructions
100 XP
Get the SNS topic ARN for 'scooter_notifications'.
For every row, if sentiment is 'NEGATIVE' and there is an image of a scooter, construct a message to send.
Publish the notification to the SNS topic.

"""
# Get topic ARN for scooter notifications
topic_arn = sns.create_topic(Name='scooter_notifications')['TopicArn']

for index, row in scooter_requests.iterrows():
    # Check if notification should be sent
    if (row['sentiment'] == 'NEGATIVE') & (row['img_scooter'] == 1):
        # Construct a message to publish to the scooter team.
        message = "Please remove scooter at {}, {}. Description: {}".format(
            row['long'], row['lat'], row['public_description'])

        # Publish the message to the topic!
        sns.publish(TopicArn = topic_arn,
                    Message = message, 
                    Subject = "Scooter Alert")
