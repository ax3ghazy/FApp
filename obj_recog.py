import boto3


def detLabels(image, bkt, rekog):
    response = rekog.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'ai5',
                'Name': Input
            }
        },
        MaxLabels=123,
    )
    out = []
    for label in response['Labels']:
        out.append(label['Name']) 
    print (out)
    return out      





Input = input("image searching for ")
client = boto3.client('s3')
client.upload_file(Input, 'abdelshahied', Input)
rekog = boto3.client('rekognition')
detLabels(Input, 'abdelshahied', rekog)
