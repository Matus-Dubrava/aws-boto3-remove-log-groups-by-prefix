import boto3

# choose prefix
# log groups with this prefix will be deleted
prefix = '/aws/lambda'

logs_client = boto3.client('logs')

logs_groups = logs_client.describe_log_groups()['logGroups']

for lg in logs_groups:
    if lg['logGroupName'].startswith(prefix):
        logs_client.delete_log_group(
            logGroupName=lg['logGroupName']
        )
