import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    cliente_id = event['body']['cliente_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('clientes')
    response = table.query(
        KeyConditionExpression=Key('cliente_id').eq(cliente_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
