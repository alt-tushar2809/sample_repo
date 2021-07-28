import json

print('Loading function')

def lambda_handler(event, context):
    #1. Parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['Amount']

    print('transactionId=' + transactionId)
    print('transactionType=' + transactionType)
    print('transactionAmount=' + transactionAmount)


    #2. Construct the body of the response object 

    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['transactionType'] = transactionType
    transactionResponse['transactionAmount'] = transactionAmount
    transactionResponse['message'] = 'H'


