import json

def lambda_handler(event, context):
    # Parse JSON input
    body = json.loads(event['body'])
    ec2_instance_type = body['ec2_type']
    ec2_count = int(body['ec2_count'])
    s3_storage_gb = float(body['s3_storage'])
    data_transfer_gb = float(body['data_transfer'])

    # AWS cost approximation (per region)
    prices = {
        "t2.micro": 0.0116,
        "t3.medium": 0.0416
    }

    ec2_cost = ec2_count * prices.get(ec2_instance_type, 0.0116) * 720  # 720 hours/month
    s3_cost = s3_storage_gb * 0.023  # $0.023 per GB
    transfer_cost = data_transfer_gb * 0.09  # $0.09 per GB
    total_cost = ec2_cost + s3_cost + transfer_cost

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            'EC2 Cost ($)': round(ec2_cost, 2),
            'S3 Cost ($)': round(s3_cost, 2),
            'Data Transfer ($)': round(transfer_cost, 2),
            'Total Monthly Cost ($)': round(total_cost, 2)
        })
    }