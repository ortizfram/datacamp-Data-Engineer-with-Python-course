"""
Multiple cat detector
After using the Cat Detector for a bit, the Animal Control team found that it was inefficient for them to pursue one cat at a time. It would be better if they could find clusters of cats.

They asked if Sam could add the count of cats detected to the message in the alerts they receive. They also asked her to lower the confidence floor, allowing the system to have more false positives.

Cats detected by Rekognition

Sam has already:

Created the Rekognition client.
Called .detect_labels() with the Bucket and Key of the image on S3.
Stored the result in the response variable.
Help Sam save cat lives! Help her count the cats in each image and include that in the alert to Animal Control!

Instructions
100 XP
_ Iterate over each element of the 'Labels' key in response.
_ Once you encounter a label with the name 'Cat', iterate over the label's instance.
_ If an instance's confidence level exceeds 85, increment cat_counts by 1.
_ Print the final cat count.
"""
# Create an empty counter variable
cats_count = 0
# Iterate over the labels in the response
for label in response['Labels']:
    # Find the cat label, look over the detected instances
    if label['Name'] == 'Cat':
        for instance in label['Instances']:
            # Only count instances with confidence > 85
            if (instance['Confidence'] > 85):
                cats_count += 1
# Print count of cats
print(cats_count)
