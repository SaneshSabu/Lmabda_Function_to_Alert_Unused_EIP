import boto3

unused_eips = []

REGION = "us-east-1"

ec2 = boto3.client('ec2',region_name=REGION)

result = ec2.describe_addresses()

def lambda_handler(event,context):

  for item in result['Addresses']:
    
    ip = item['PublicIp']
    
    if 'AssociationId' not in item:
    
      unused_eips.append(ip)

  sns_client = boto3.client('sns',region_name=REGION)

  response = sns_client.list_topics()

  ARN = response['Topics'][2]['TopicArn']


  for unused in unused_eips:

    sns_client.publish(
                TopicArn=ARN,
                Subject='Unused EIP available',
                Message="Unused EIPs available to clear, Please check out- {}".format(unused)
                      )
    
    print("Unused EIPs available to clear, Please check out- {}".format(unused))
