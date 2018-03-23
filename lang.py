import boto3

def ded_senti (buck, fil, path):
	client = boto3.client('s3')

	response = client.create_bucket(Bucket=buck)
	client.upload_file(fil, buck, fil)


	#path = "/home/ubuntu/Desktop/test.txt"
	com_file = open(path, 'r')

	comp = boto3.client('comprehend')

	response = comp.detect_dominant_language(
    	Text = com_file.readline(),
	)
	x = 0.0
	for language in response['Languages']:
		if language ['Score'] > x:
			code = language ['LanguageCode']
			x = language ['Score']
	
	print (code)	
	return code


#ded_senti ('abdelshahied', 'test.txt', "/home/ubuntu/Desktop/test.txt")

