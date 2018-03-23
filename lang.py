import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='abdelshahied')
client.upload_file('test.txt', 'abdelshahied', 'test.txt')


path = "/home/ubuntu/Desktop/test.txt"
com_file = open(path, 'r')

comp = boto3.client('comprehend')

response = comp.batch_detect_dominant_language(
    TextList=[
        com_file.readline(),
    ]
)

print (response)

for match in response['ResultList']:
	for language in match['Languages']:
		if (language['Score'] > 0.9):
			code = language ['LanguageCode']

print (code)	
