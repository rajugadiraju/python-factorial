import json

def factorial(n):
    """
    Calculates the factorial of a positive integer n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def lambda_handler(event, context):
    try:
        num_str = event["num"]
        num = int(num_str)
        
        if not num_str.isdigit():
            response = {
                "statusCode": 400,
                "body": json.dumps("Please give a valid integer in the 'num' field.")
            }
        elif num < 0:
            response = {
                "statusCode": 400,
                "body": json.dumps("Please give a positive integer in the 'num' field.")
            }
        else:
            result = factorial(num)
            response = {
                "statusCode": 200,
                "body": json.dumps({"result": result})
            }
    except (KeyError, ValueError):
        response = {
            "statusCode": 400,
            "body": json.dumps("Invalid input. Please give a valid integer in the 'num' field.")
        }
    
    return response

# Simulating an event
event = {"num": "10"}  # You can change the value to test different inputs

# Simulating a context (not used in this function)
context = None

# Calling the lambda_handler function with the simulated event and context
result = lambda_handler(event, context)
print(result)