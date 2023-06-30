import boto3
import json
import os
from . import config

def handle(event, context):

    connection_id = event["requestContext"]["connectionId"]

    ## create session object
    # aws_session = boto3.Session(
    #     aws_access_key_id= config.AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    #     region_name=config.AWS_REGION_NAME
    # )

    # or this object will also do
    # lambda_client = boto3.client(
    #     'lambda',
    #     region_name=config.AWS_REGION_NAME,
    #     aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
    # )

    # lambda_client.invoke(
    #     FunctionName="GetConnectionIdFunction",
    #     InvocationType="Event",
    #     LogType="None",
    #     ClientContext=str(connection_id),
    #     Payload=json.dumps({"connection_id":connection_id})

    # )

    print(connection_id)

    # !! PUT THE URL IN CONFIGURATION
    socket_client = boto3.client(
        'apigatewaymanagementapi',
        region_name=config.AWS_REGION_NAME,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        endpoint_url=str(os.environ['apiEndpoint'])

    )

    # get the connection_id data from event object
    #! TODO: remove static
    #connection_id = 'test1'
    socket_client.post_to_connection(
        ConnectionId=connection_id,
        Data=json.dumps({"connectionId": connection_id})
    )

    #print(response)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "{'connectionId':'"+connection_id+"'}"
        })   
    }

