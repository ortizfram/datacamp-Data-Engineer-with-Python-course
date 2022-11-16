"""
Parking sign reader
City planners have millions of images from truck cameras. Since the city does not keep a record of this data, parking regulations would be very valuable for planners to know.

Sam found detect_text() in the boto3 Rekognition documentation. She is going to use it to extract text out of the images City planners provided.



Sam has:

Created the Rekognition client.
Called .detect_text() and stored the result in response.
Help Sam create a data source for parking regulations in the City. Use Rekognition's .detect_text() method to extract lines and words from images of parking signs.

Instructions 2/2
_ Iterate over each detected text in response, and append each detected text to words if the text's type is 'WORD'.
_ Iterate over each detected text in response, and append each detected text to lines if the text's type is 'LINE'.

"""
# Create empty list of words
words = []
# Iterate over the TextDetections in the response dictionary
for text_detection in response['TextDetections']:
  	# If TextDetection type is WORD, append it to words list
    if text_detection['Type'] == 'WORD':
        # Append the detected text
        words.append(text_detection['DetectedText'])
# Print out the words list
print(words)
'''
['NO', 'PARKING', '7', 'AM', 'TO', '12', 'NOON', 'MONDAY']
'''
#-------

# Create empty list of lines
lines = []
# Iterate over the TextDetections in the response dictionary
for text_detection in response['TextDetections']:
  	# If TextDetection type is Line, append it to lines list
    if text_detection['Type'] == 'LINE':
        # Append the detected text
        lines.append(text_detection['DetectedText'])
# Print out the words list
print(lines)
'''
['NO PARKING', '7 AM', 'TO', '12 NOON', 'MONDAY']
'''

