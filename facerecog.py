import boto3

def detFace(img, bkt, rekog):
    responsex = rekog.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bkt,
                'Name': img
                }
            },
        Attributes=[
            'ALL',
            ]
        )
    out3 = []
    for i in responsex['FaceDetails']:
        out3.append(i)
    print(out3)
    return out3


def getEmot(details):
    for match in details:
        print('The Person infront of you is ')        
        print(match['Emotions'][0]['Type'], '\n')


def getFaceDet(details):
    for match in details:
        print('You are seeing a ', match['Gender']['Value'])
        print('The age ranges between ', match['AgeRange']['Low'], ' and ', match['AgeRange']['High'])
        if (match['Gender']['Value'] == 'Male'):
            if (match['Beard']['Value']):
                print ("with beard")
            if (match['Mustache']['Value']):
                print ("with Mustache")



def indexFace(img, bkt, cID, rekog):
    
    response = rekog.index_faces(
        CollectionId= cID,
        Image={
            'S3Object': {
                'Bucket': bkt,
                'Name': img
            }
        },
        DetectionAttributes=[
            'ALL',
            ]
        )

    out = []
    for i in response['FaceRecords']:
        out.append(i['Face']['FaceId'])        
    
        #responses = rekog.search_faces(
         #   CollectionId='omg',
          #  FaceId=phid,
        #)

    print(out)
    return out


def searchFace(bkt, cID, index, rekog):
    flag = 1    
    for i in index:
        responses = rekog.search_faces(
            CollectionId= cID,
            FaceId= i,
        )
        for match in responses['FaceMatches']:
            if(match['Similarity'] > 70):
                flag = 0; 
            if ('ExternalImageId' in match['Face']):           
                print(match['Face']['ExternalImageId'], '\n')

    return flag


def ask(image, bkt, iID, cID, det, client, rekog):
    getFaceDet(det)

    doyou = input("Do you want to add this person? ")
    type(doyou)

    if(doyou == 'yes'):
        iID = input("Say the person's name ")
        type(iID)
  
        print (iID , '\n')    
        
        # a solo pic
        response1 = rekog.index_faces(
            CollectionId=cID,    
            Image={
                'S3Object': {
                    'Bucket': bkt,
                    'Name': image
                }
            },
            ExternalImageId= iID,
            DetectionAttributes=[
                'ALL',
            ]
        )
        print(response1, '\n')
    else:
        response2 = client.delete_object(
            Bucket= bkt,
            Key= image
        )



Input = input("image searching for ")
client = boto3.client('s3')
client.upload_file(Input, 'abdelshahied', Input)
rekog = boto3.client('rekognition')

det = detFace(Input, 'abdelshahied', rekog)
indecies = indexFace(Input, 'abdelshahied', 'omg', rekog)
first = searchFace('abdelshahied', 'omg', indecies, rekog)
iID = []
cID = []
if (first):
    ask(Input, 'abdelshahied', iID, cID, det, client, rekog)
else: 
    response2 = client.delete_object(
        Bucket= 'abdelshahied',
        Key= Input
    )
