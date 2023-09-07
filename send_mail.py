import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from github import context

# Get the email parameters from environment variables
recipient_email = os.environ['RECIPIENT_EMAIL']
email_subject = os.environ['EMAIL_SUBJECT']
email_body = os.environ['EMAIL_BODY']

# Get the email parameters from GitHub Actions secrets
smtp_server = 'sandbox.smtp.mailtrap.io'
smtp_port = 2525
smtp_username = context.secrets['MAIL_USERNAME']
smtp_password = context.secrets['MAIL_PASSWORD']

# Create a message
message = MIMEMultipart()
message['From'] = smtp_username
message['To'] = recipient_email
message['Subject'] = email_subject

# Add a plain text message
message.attach(MIMEText(email_body, 'html'))

# Create a secure SSL context
context = smtplib.SMTP(smtp_server, smtp_port)
context.starttls()

# Login to the SMTP server with your Gmail credentials
context.login(smtp_username, smtp_password)

# Send the email
context.sendmail(smtp_username, recipient_email, message.as_string())

# Quit the SMTP server
context.quit()
