import boto3
import requests

def voice2txt(fil, buckt, jopname, formatt):

	client = boto3.client('s3')
	client.upload_file(fil, buckt, fil)
	client = boto3.client('transcribe')
	path = 'https://s3-us-east-2.amazonaws.com/' + buckt + '/' + fil
	response = client.start_transcription_job(
	    TranscriptionJobName=jopname,
	    LanguageCode='en-US',
	    MediaFormat=formatt,
	    Media={
		'MediaFileUri': path
	    }
	)

def get_txt (fil, buckt, jopname):
	
	client = boto3.client('s3')
	client.upload_file(fil, buckt, fil)
	client = boto3.client('transcribe')

	response = client.get_transcription_job(
    TranscriptionJobName=jopname
)
	print (response['TranscriptionJob']['TranscriptionJobName'])
	if response['TranscriptionJob']['TranscriptionJobStatus'] == "FAILED":
		print ('-1')
		return -1
	if response['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
		print(response['TranscriptionJob']['Transcript']['TranscriptFileUri'])
		return response['TranscriptionJob']['Transcript']['TranscriptFileUri']
	if response['TranscriptionJob']['TranscriptionJobStatus'] == "IN-PROGRESS":
		print ('0')
		return 0
	else: print ('error')
def get_get (uri):
	r = requests.get(url=uri)
	print(r.json())
	return x

#voice2txt ('amr.mp3', 'abdelshahied', 'a007')
u = get_txt ('amr.mp3', 'abdelshahied', 'a007')
x =get_get(u)

