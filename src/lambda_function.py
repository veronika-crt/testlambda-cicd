def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }


import json

def greet_handler(event, context):
    name = event.get("name", "Guest")
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello {name}, welcome to AWS Lambda!")
    }
