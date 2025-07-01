import boto3

def lambda_handler(event, context):
    # Entrada (json)
    cliente_id = event['body']['cliente_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('clientes')
    response = table.update_item(
        Key={
            'cliente_id': cliente_id
        },
        UpdateExpression="set datos=:datos_a_actualizar",
        ExpressionAttributeValues={
            ':datos_a_actualizar': datos
        },
        ReturnValues="UPDATED_NEW"
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
