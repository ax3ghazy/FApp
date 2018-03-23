import boto3

client = boto3.client('s3')

response = client.create_bucket(Bucket='abdelshahied')
client.upload_file('test.txt', 'abdelshahied', 'test.txt')

translt = boto3.client('translate')

source = 'es'
target = 'ar'

path = "/home/ubuntu/Desktop/test.txt"
tran_file = open(path, 'r')

response = translt.translate_text(
    Text= tran_file.read(),
    SourceLanguageCode=source,
    TargetLanguageCode= 'en'
)

temp = response['TranslatedText']

response = translt.translate_text(
    Text= temp,
    SourceLanguageCode='en',
    TargetLanguageCode= target
)

temp1 = response['TranslatedText']

print (temp1)
