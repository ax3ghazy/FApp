import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='abdelshahied')
client.upload_file('en_trans.txt', 'abdelshahied', 'en_trans.txt')


path = "/home/ubuntu/Desktop/en_trans.txt"
ded_file = open(path, 'r')

ded = boto3.client('comprehend')

response = ded.detect_sentiment(
    Text=ded_file.read(),
    LanguageCode='en'
)

out = response['Sentiment']

print (out, '\n')
#print (response)

