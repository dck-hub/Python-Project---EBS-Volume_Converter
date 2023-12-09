import json
import boto3

def get_volumn_id_from_arn(volumn_arn):
  # split the arn using (':') operater
    arn_parts = volumn_arn.split(':')   
    volumn_id = arn_parts[-1].split('/')[-1]
    return volumn_id

def lambda_handler(event, context):
    
    volumn_arn = event['resources'][0]
    volumn_id  = get_volumn_id_from_arn(volumn_arn)

  # Initialize AWS ec2 client
    ec2_client = boto3.client("ec2")
    
    response = ec2_client.modify_volume(
  # Get the volume ID and convert the EBS volume into 'gp3' volume type
        VolumeId = volumn_id,
        VolumeType = 'gp3'
    )
    
