import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# DynamoDB table name
# Add your Table_Name, Primary_Key and Primary_key value below

TABLE_NAME = "add_table name here"
PRIMARY_KEY = "add primary key here"
PRIMARY_KEY_VALUE = "add primary key value here"

def lambda_handler(event, context):
    try:
        print("Lambda triggered. Event received:", event)

        # Get the current count
        response = dynamodb.get_item(
            TableName=TABLE_NAME,
            Key={
                PRIMARY_KEY: {'S': PRIMARY_KEY_VALUE}
            }
        )
        print("DynamoDB get_item response:", response)

        # Extract the current count
        if 'Item' in response:
            current_count = int(response['Item']['count']['N'])
            print("Current count from table:", current_count)
        else:
            current_count = 0
            print("No item found, starting count at 0")

        # Increment the count
        new_count = current_count + 1
        print("New count after increment:", new_count)

        # Update the count in DynamoDB
        update_response = dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={PRIMARY_KEY: {'S': PRIMARY_KEY_VALUE}},
            UpdateExpression="SET #c = :val",
            ExpressionAttributeNames={"#c":"count"}
            ExpressionAttributeValues={":val": {'N': str(new_count)}}
        )
        print("DynamoDB update_item response:", update_response)

        # Return the new count as JSON
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"  # Needed for CORS if using API Gateway
            },
            "body": json.dumps({"count": new_count})
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

