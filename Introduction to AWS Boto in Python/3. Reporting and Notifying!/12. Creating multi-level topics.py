"""
Creating multi-level topics
The City Council asked Sam to create a critical and extreme topic for each department.

The critical topic will trigger alerts to staff and managers.

The extreme topics will trigger alerts to politicians and directors - it means the thresholds are completely exceeded.

For example, the trash department will have a trash_critical and trash_extreme topic.

She has already created the boto3 SNS client in the sns variable. She created a variable departments that contains a unique list of departments.

In this lesson, you will help Sam make the City run faster!

You will create multi-level topics with a different set of subscribers that trigger based on different thresholds.

You will effectively be building a smart alerting system!

Instructions
100 XP
_ For each department create a critical topic and store it in critical.
_ For each department, create an extreme topic and store it in extreme.
_ Place the created TopicArns into dept_arns.
_ Print the dictionary.

"""
dept_arns = {} 

for dept in departments:
  # For each deparment, create a critical topic
  critical = sns.create_topic(Name="{}_critical".format(dept))
  # For each department, create an extreme topic
  extreme = sns.create_topic(Name="{}_extreme".format(dept))
  # Place the created TopicARNs into a dictionary 
  dept_arns['{}_critical'.format(dept)] = critical['TopicArn']
  dept_arns['{}_extreme'.format(dept)] = extreme['TopicArn']

# Print the filled dictionary.
print(dept_arns)
