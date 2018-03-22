import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='ax3g-bucket')

client.upload_file('saba7.jpg', 'ax3g-bucket', 'saba7.jpg')

rekog = boto3.client('rekognition')
response = rekog.detect_faces(
        Image={
            'S3Object': {
                'Bucket': 'ax3g-bucket',
                'Name': 'saba7.jpg'
                }
            },
        Attributes=[
            'ALL',
            ]
        )
print(response)
