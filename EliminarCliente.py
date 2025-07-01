import boto3

def lambda_handler(event, context):
    # Entrada (json)
    cliente_id = event['body']['cliente_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('clientes')
    response = table.delete_item(
        Key={
            'cliente_id': cliente_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
