import boto3

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
