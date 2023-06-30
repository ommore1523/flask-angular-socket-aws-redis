import boto3
import json
from . import config


def get_id(event, context):
    """
    Returns the connection id of the current socket connection

    parameters:

        - event: lambda function event
        - context: lambda function context
    """

    ## log the event
    __logger(event)

    ## create session object
    # aws_session = boto3.Session(
    #     aws_access_key_id= config.AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    #     region_name=config.AWS_REGION_NAME
    # )

    # # or this object will also do
    # socket_client = boto3.client(
    #     'apigatewaymanagementapi',
    #     region_name=config.AWS_REGION_NAME,
    #     aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
    # )

    # # get the connection_id data from event object
    # #! TODO: remove static
    # connection_id = 'test1'
    # socket_client.post_to_connection(
    #     ConnectionId=connection_id,
    #     Data=json.dumps({"connectionId": connection_id})
    # )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"connection_id: {123} sent to client"
        })
    }

def __logger(message):
    """
    Prints/logs the message

    parameters:
        - message: message to be logged
    """

    # TODO: check proper way for logging in aws
    print(str(message))
