"""
Sending multi-level alerts
Sam is going to prototype her alerting system with the water data and the water department.

According to the Director, when there are over 100 alerts outstanding, that's considered critical. If there are over 300, that's extreme.

She has done some calculations and came up with a vcounts dictionary, that contains current requests for 'water', 'streets' and 'trash'.

She has also already created the boto3 SNS client and stored it in the sns variable.

In this exercise, you will help Sam publish a critical and an extreme alert based on the thresholds!

Instructions
100 XP
_ If there are over 100 water violations, publish to 'water_critical' topic.
_ If there are over 300 water violations, publish to 'water_extreme' topic.

"""
if vcounts['water'] > 100:
  # If over 100 water violations, publish to water_critical
  sns.publish(
    TopicArn = dept_arns['water_critical'],
    Message = "{} water issues".format(vcounts['water']),
    Subject = "Help fix water violations NOW!")

if vcounts['water'] > 300:
  # If over 300 violations, publish to water_extreme
  sns.publish(
    TopicArn = dept_arns['water_extreme'],
    Message = "{} violations! RUN!".format(vcounts['water']),
    Subject = "THIS IS BAD.  WE ARE FLOODING!")
