import json
import boto3

def lambda_handler(event, context):
    # Extract the bucket name and file name from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Define the backup bucket name
    backup_bucket = 'my-backup-bucket'

    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Copy the file from the source bucket to the backup bucket
        s3.copy_object(
            Bucket=backup_bucket,
            CopySource={'Bucket': source_bucket, 'Key': file_key},
            Key=file_key
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Backup successful!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
