import config
from flask_socketio import SocketIO
import boto3
import logging

import json

redis_uri = f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/0"

sio = SocketIO(message_queue=redis_uri, cors_allowed_origins="*")


def send_socket(event, namespace, room, message_key="default", message=""):
    """method for publishing messages using celery"""
    if namespace != 0:
        print(event, namespace, room, message_key, message)
        sio.emit(event, {f"{message_key}_msg": message}, namespace=namespace, room=room)
    else:
        print(message)


lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.AWS_REGION_NAME,
    endpoint_url=config.AWS_LAMBDA_ENDPOINT_URL,
)


import boto3
import json

# def send_socket_message(event, context):
# Extract connection ID and message from the event
# connection_id = event['requestContext']['connectionId']
# message = 'Hello, WebSocket!'

# Create an instance of the API Gateway Management API
# apigw_management_api = boto3.client('apigatewaymanagementapi',
# endpoint_url='YOUR_APIGATEWAY_ENDPOINT')

# # Send the message to the WebSocket connection
# response = apigw_management_api.post_to_connection(
#     ConnectionId=connection_id,
#     Data=json.dumps({'message': message}).encode('utf-8')
# )

# return {
#     'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
#     'body': 'Message sent successfully'
# }


def send_msg(event, namespace, room, message):
    connection_id = room

    print("connecion id : ", connection_id)

    # if not isinstance(connection_id, int):
    # !! PUT THE URL IN CONFIGURATION
    logging.info("initiating apimanagementgateway connection")

    # get the connection_id data from event object
    #! TODO: remove static
    # connection_id = 'test1'
    # socket_msg = {"connection_id": connection_id, \
    #         "message": json.dumps({str(event): message})}
    logging.info("starting post message on apimanagementgateway")

    apigw_management_api = boto3.client(
        "apigatewaymanagementapi",
        endpoint_url="https://khfn2eoi8i.execute-api.us-east-1.amazonaws.com/Prod",
    )


    response = apigw_management_api.post_to_connection(
        ConnectionId=connection_id,
        Data=json.dumps({"message": message}).encode("utf-8"),
    )
    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": "Message sent successfully",
    }
    # function_name = config.SOCKET_SEND_MESSAGE_FUNCTION_NAME

    # lambda_client.invoke(
    #     FunctionName=function_name,
    #     InvocationType='Event',
    #     Payload=json.dumps(socket_msg)
    # )
