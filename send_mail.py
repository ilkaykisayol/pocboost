import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Email configuration
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = os.environ['MAIL_USERNAME']  # Replace with your Gmail email address
smtp_password = os.environ['MAIL_PASSWORD']  # Replace with your Gmail password or an app-specific password

# Email content
recipient_email = os.environ['RECIPIENT_EMAIL']
subject = 'Hello from GitHub Actions'
message = 'This is a test email sent from a GitHub Actions workflow.'

# Create a message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach the message
msg.attach(MIMEText(message, 'plain'))

try:
    # Create a secure SSL context
    context = smtplib.SMTP(smtp_server, smtp_port)
    context.starttls()

    # Login to the SMTP server with your Gmail credentials
    context.login(smtp_username, smtp_password)

    # Send the email
    context.sendmail(smtp_username, recipient_email, msg.as_string())

    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {str(e)}')
finally:
    # Quit the SMTP server
    context.quit()
