import json

print('Loading function')

def lambda_handler(event, context):
    #1. Parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['Amount']

    print('transactionId=' + transactionId)
    print('transactionTy=' + transactionId)
    print('transactionId=' + transactionId)

