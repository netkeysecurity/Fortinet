import boto3
import json
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
BUCKET_NAME = 'fmg-allowlist'
OBJECT_KEY = 'FortiGate_IP_List.txt'

def lambda_handler(event, context):
    try:
        # Check if the body exists in the event
        if 'body' not in event:
            logger.error("Request body is missing.")
            return {
                'statusCode': 400,
                'body': 'Error: Request body is missing.'
            }

        # Parse the body to get the IP address
        try:
            # Handle JSON strings passed as 'body'
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
            ip_address = body.get('ip_address')
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON body.")
            return {
                'statusCode': 400,
                'body': 'Error: Invalid JSON format in request body.'
            }

        if not ip_address:
            logger.error("No IP address provided in the request body.")
            return {
                'statusCode': 400,
                'body': 'Error: No IP address provided in the request body.'
            }

        # Fetch the current IP list file from S3
        try:
            obj = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
            ip_list = obj['Body'].read().decode('utf-8').splitlines()
            logger.info(f"Fetched current IP list: {ip_list}")
        except s3.exceptions.NoSuchKey:
            logger.warning(f"{OBJECT_KEY} not found in {BUCKET_NAME}. Creating a new file.")
            ip_list = []

        # Add the new IP address if it's not already in the list
        if ip_address not in ip_list:
            ip_list.append(ip_address)
            updated_content = "\n".join(ip_list)

            # Save the updated list back to S3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=OBJECT_KEY,
                Body=updated_content,
                ContentType='text/plain'
            )
            logger.info(f"IP {ip_address} added to the list.")
            return {
                'statusCode': 200,
                'body': f'IP {ip_address} added to the list.'
            }
        else:
            logger.info(f"IP {ip_address} is already in the list.")
            return {
                'statusCode': 200,
                'body': f'IP {ip_address} is already in the list.'
            }
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
