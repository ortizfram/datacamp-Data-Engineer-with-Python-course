"""
Sending an alert
Elena Block, Sam's old friend and council member is running for office and potholes are a big deal in her district. She wants to help fix it.

Pothole
Elena asked Sam to adjust the streets_critical topic to send an alert if there are over 100 unfixed potholes in the backlog.

Sam has created the boto3 SNS client in the sns variable. She stored the streets_critical topic ARN in the str_critical_arn variable.

Help Sam take the next step.

She needs to check the current backlog count and send a message only if it exceeds 100.

The fate of District 12, and the results of Elena's election rest on your and Sam's shoulders.

Instructions
100 XP
_ If there are over 100 potholes, send a message with the current backlog count.
_ Create the email subject to also include the current backlog counit.
_ Publish message to the streets_critical Topic ARN.

"""
# If there are over 100 potholes, create a message
if streets_v_count > 100:
  # The message should contain the number of potholes.
  message = "There are {} potholes!".format(streets_v_count)
  # The email subject should also contain number of potholes
  subject = "Latest pothole count is {}".format(streets_v_count)

  # Publish the email to the streets_critical topic
  sns.publish(
    TopicArn = str_critical_arn,
    # Set subject and message
    Message = message,
    Subject = subject
  )
