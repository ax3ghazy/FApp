import boto3

def translate (source, target, buck, fil_in, fil_out_en, path, path1):

	client = boto3.client('s3')

	response = client.create_bucket(Bucket=buck)
	client.upload_file(fil_in, buck, fil_in)
	client.upload_file(fil_out_en, buck, fil_out_en)

	translt = boto3.client('translate')

	#source = 'es'
	#target = 'ar'

	#path = "/home/ubuntu/Desktop/test.txt"
	#path1 = "/home/ubuntu/Desktop/en_trans.txt"

	tran_file = open(path, 'r')
	out_file = open(path1, 'w')

	response = translt.translate_text(
	    Text= tran_file.read(),
	    SourceLanguageCode=source,
	    TargetLanguageCode= 'en'
	)

	temp = response['TranslatedText']
	out_file.write(temp)

	response = translt.translate_text(
	    Text= temp,
	    SourceLanguageCode='en',
	    TargetLanguageCode= target
	)

	temp1 = response['TranslatedText']

	print (temp1)
	return temp1

#translate ('es', 'de', 'abdelshahied', 'test.txt', 'en_trans.txt', "/home/ubuntu/Desktop/test.txt", "/home/ubuntu/Desktop/en_trans.txt")
