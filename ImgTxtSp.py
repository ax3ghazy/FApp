import boto3

def ImgtoTxt (img,bkt,path):
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
    out = ""
    for i in response['TextDetections']:
        out = out + i['DetectedText']+" "
    print(out)
    outf = open(path, 'w')
    outf.write(out)
    outf.close()
    return out

x=ImgtoTxt('img.jpg', 'mayada', "C:/Users/asus/PycharmProjects/untitled1/file.txt")

def TxtToSp (format,txt,vid,outname):
    client = boto3.client('polly')
    response = client.synthesize_speech(
        OutputFormat=format,
        Text=txt,
        VoiceId=vid
    )
    print('\n')
    out = response['AudioStream']
    out = out.read()
    print(out)
    outf = open(outname, "wb")
    outf.write(out)
    outf.close()
    return

TxtToSp ('mp3',x,'Emma','ily.mp3')