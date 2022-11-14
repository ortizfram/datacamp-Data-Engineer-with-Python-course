"""
|||||
From learning how AWS works to creating S3 buckets and uploading files to them. You will master the basics of setting up AWS and uploading files to the cloud!
|||||

|  INITIALIZE BOTO3 CLIENT  |

  -> Boto 3 : 
              import boto3
              
              s3 = boto3.client('s3',
                                region_name='us-east-1',
                                aws_access_key_id = AWS_KEY_ID,
                                aws_secret_access_key = AWS_SECRET)
                                
              response = s3.list_buckets()
  -------->
  # in AWS Console creation of USER
      - Create KEYs w/ IAM
      - add user
      - programatic user 
      - select policies:
              .  s3 full access
              .  amazon sns full access
              .  amazon rekognition full access
              .  comprehend full access
      - Grab KEY and SECRET and store smw safe

|  AWS services  |

  IAM :  manage permissions
  S3 :  store files in cloud
  SNS :  emails / texts based on conditions and events in pipelines
  COMPREHEND :  sentiment analysis on blocks of text
  REKOGNITION   : extract text from images an dlooks 4 cats in pictures
  
"""
