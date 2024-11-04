# FortiGate-to-FortiManager Zero Trust Setup

This repository provides the necessary files to implement a zero-trust configuration between FortiGate and FortiManager using AWS services.

### Files Included
- **api-gateway-fmg-list-prod-swagger.json**: OpenAPI (Swagger) definition for the AWS API Gateway configuration. This defines the endpoints and security settings for updating and retrieving the FortiGate allowlist.
  
- **lambda_function.py**: Python code for the AWS Lambda function. This function processes incoming requests, validates IP addresses, and updates the allowlist stored in Amazon S3.

- **update_fmg_feed.conf**: Configuration file for the FortiGate automation setup. This file contains commands and settings to automate the IP address retrieval and update the allowlist via an outgoing webhook.

### Usage
1. Deploy the API Gateway using the Swagger definition file (`api-gateway-fmg-list-prod-swagger.json`).
2. Set up the Lambda function with the provided Python code (`lambda_function.py`).
3. Configure the FortiGate devices using the automation configuration (`update_fmg_feed.conf`) to ensure dynamic IP updates in the allowlist.

### Requirements
- AWS API Gateway
- AWS Lambda
- Amazon S3
- FortiGate devices with automation enabled

### Notes
- Ensure that the API Gateway and Lambda function are properly secured with API keys and IP-based allowlisting.
- Update the configurations in `update_fmg_feed.conf` to match your specific setup, including the correct API endpoint and authentication details.
