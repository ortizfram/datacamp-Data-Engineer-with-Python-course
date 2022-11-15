"""
Creating a Topic
Sam has been doing such a great job with her new skills, she got a promotion.

With her new title of Information Systems Analyst 3 (as opposed to 2), she has gotten a tiny pay bump in exchange for a lot more work.

Knowing what she can do, the City Council asked Sam to prototype an alerting system that will alert them when any department has more than 100 Get It Done requests outstanding.

They would like for council members and department directors to receive the alert.

Help Sam use her new knowledge of Amazon SNS to create an alerting system for Council!

Instructions
100 XP
_ Initialize the boto3 client for SNS.
_ Create the 'city_alerts' topic and extract its topic ARN.
_ Re-create the 'city_alerts' topic and extract its topic ARN with a one-liner.
_ Verify the two topic ARNs match.

"""
# Initialize boto3 client for SNS
sns = boto3.client('sns', 
                   region_name='us-east-1', 
                   aws_access_key_id=AWS_KEY_ID, 
                   aws_secret_access_key=AWS_SECRET)

# Create the city_alerts topic
response = sns.create_topic(Name="city_alerts")
c_alerts_arn = response['TopicArn']

# Re-create the city_alerts topic using a oneliner
c_alerts_arn_1 = sns.create_topic(Name='city_alerts')['TopicArn']

# Compare the two to make sure they match
print(c_alerts_arn == c_alerts_arn_1)
