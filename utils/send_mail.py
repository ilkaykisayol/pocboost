import boto3
from botocore.exceptions import NoCredentialsError
import os

# Email content
recipient_email = os.environ['RECIPIENT_EMAIL']
subject = os.environ['EMAIL_SUBJECT']
message = os.environ['EMAIL_BODY']

ses = boto3.client('ses', region_name='eu-west-1')
sender = 'supportdmdp@astrazeneca.com'

# Create the email message
message = {
    'Subject': {'Data': subject},
    'Body': {'Html': {'Data': message}},
}

# Send the email
try:
    response = ses.send_email(
        Source=sender,
        Destination={'ToAddresses': [recipient_email]},
        Message=message
    )
    print(f"Email sent with message ID: {response['MessageId']}")
except NoCredentialsError:
    print("AWS credentials not available.")
