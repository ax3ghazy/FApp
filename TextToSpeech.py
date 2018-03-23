import boto3

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

TxtToSp ('mp3','I love you','Emma','ily.mp3')