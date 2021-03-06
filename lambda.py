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
    transactionResponse['message'] = 'Hello from Lambda land'

    #3. Construct http response object

    responseObject = {}
    responseObject['statuscode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)


    #4. Return the response object 

    return responseObject






