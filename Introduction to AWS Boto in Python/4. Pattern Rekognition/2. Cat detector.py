"""
Cat detector
Sam has been getting more and more challenging projects as a result of her popularity and success.

The newest request is from the animal control team. They want to receive notifications when an image comes in from the Get It Done application contains a cat. They can find feral cats and go rescue them. They provided her with two images that she can test her system with. One contains a cat, one does not. Both images are referenced in variables image1 and image2 respectively.

Sam has also created the boto3 Rekognition client in the rekog variable.

Help Sam use Rekognition to enable the animal control team to rescue stray cats!

Instructions 3/3
Use the Rekognition client to detect the labels for image1. Return a maximum of 1 label.
Detect the labels for image2 and print the response's labels..


"""
# Use Rekognition client to detect labels
image1_response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image=image1, MaxLabels=1)

# Print the labels
print(image1_response['Labels'])
'''
[{'Confidence': 99.85968017578125, 'Instances': [], 'Name': 'Walkway', 'Parents': [{'Name': 'Path'}]}]
'''

# Use Rekognition client to detect labels
image2_response = rekog.detect_labels(
    Image=image2, MaxLabels=1
)

# Print the labels
print(image1_response['Labels'])
'''
[{'Confidence': 96.95977020263672, 'Instances': [{'BoundingBox': {'Height': 0.3252439796924591, 'Left': 0.668968915939331, 
'Top': 0.14526571333408356, 'Width': 0.1563364714384079}, 
'Confidence': 96.95977020263672}], 'Name': 'Cat', 'Parents': [{'Name': 'Pet'}, {'Name': 'Mammal'}, {'Name': 'Animal'}]}]
'''

"""Question
_ Which image contained cats?
Possible Answers:

             image1.
        OK   image2."""
