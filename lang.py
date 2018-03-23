import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='abdelshahied')
client.upload_file('test.txt', 'abdelshahied', 'test.txt')


path = "/home/ubuntu/Desktop/test.txt"
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
