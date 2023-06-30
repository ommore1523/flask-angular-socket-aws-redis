import json
import logging

def handle(event, context):

    connection_id = event["requestContext"]["connectionId"]
    
    print(connection_id)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "connected",
            "connection_id": str(connection_id)
        })   
    }


