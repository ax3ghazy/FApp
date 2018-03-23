import boto3

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
