import boto3


def add(image, bkt, cID, iID, rekog):
    if (cID == ''):
        cID = input ("Name of the new collection: ")
        response = rekog.create_collection(
            CollectionId=cID
        )
    response1 = rekog.index_faces(
        CollectionId=cID,
        Image={
            'S3Object': {
                'Bucket': bkt,
                'Name': image
            }
        },
        ExternalImageId=iID,
        DetectionAttributes=[
            'ALL',
        ]
    )
    print(response1, '\n')


Input = input("adding ")
iID = input ("with an ID of ")
client = boto3.client('s3')
rekog = boto3.client('rekognition')
client.upload_file(Input, 'abdelshahied', Input)

cID = 'omg'

add(Input, 'abdelshahied', cID, iID, rekog)
