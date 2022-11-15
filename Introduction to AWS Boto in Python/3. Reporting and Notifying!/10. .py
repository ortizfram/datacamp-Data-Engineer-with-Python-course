"""
Sending a single SMS message
Elena asks Sam outside of work (per regulation) to send some thank you SMS messages to her largest donors.

Sam believes in Elena and her goals, so she decides to help.

She decides writes a quick script that will run through Elena's contact list and send a thank you text.

Since this is a one-off run and Sam is not expecting to alert these people regularly, there's no need to create a topic and subscribe them.

Sam has created the boto3 SNS client and stored it in the sns variable. The contacts variable contains Elena's contacts as a DataFrame.

Help Sam put together a quick hello to Elena's largest supporters!

Instructions
100 XP
_ For every contact, send an ad-hoc SMS to the contact's phone number.
_ The message sent should include the contact's name.

"""
# Loop through every row in contacts
for idx, row in contacts.iterrows():
    
    # Publish an ad-hoc sms to the user's phone number
    response = sns.publish(
        # Set the phone number
        PhoneNumber = str(row['Phone']),
        # The message should include the user's name
        Message = 'Hello {}'.format(row['Name'])
    )
   
    print(response)
