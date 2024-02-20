import json

def lambda_handler(event, context):
  return {
    "statusCode": 200,
    "body": json.dumps("Hello World!")
  }

# Simulating an event (not needed for this function)
event = {}

# Calling the lambda_handler function
result = lambda_handler(event, None)
print(result)
