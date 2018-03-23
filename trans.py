import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='abdelshahied')
client.upload_file('song.mp3', 'abdelshahied', 'song.mp3')

tran = boto3.client('transcribe')

response = tran.start_transcription_job(
    TranscriptionJobName='gogoSong',
    LanguageCode='en-US',
    MediaSampleRateHertz=10000,
    MediaFormat='mp3',
    Media={
        'MediaFileUri': 'https://s3-us-west-2.amazonaws.com/abdelshahied/song.mp3'
    }
)

print (response)
