import boto3

def ImgtoTxt (img,bkt):
    client = boto3.client('s3')
    client.upload_file(img,bkt,img)
    client = boto3.client('rekognition')
    response = client.detect_text(
        Image={
            'S3Object': {
                'Bucket': bkt,
                'Name': img,
            }
        }
    )
    out = []
    for i in response['TextDetections']:
        out.append(i['DetectedText'])
    print(out)
    return out

ImgtoTxt('text1.jpg', 'mayada')