import boto3

rt = boto3.client('lex-runtime')

response = rt.post_text(
botName='SabahMarwaha',
botAlias='saboha',
userId='739551186249',
sessionAttributes={
    'FirstName': 'Ahmed'
},
requestAttributes={
    'FirstName': 'Ahmed'
},
inputText='where am i?'
)
print(response)

