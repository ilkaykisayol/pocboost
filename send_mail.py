import os
import smtplib

def send_email(recipient, subject, message):
    # Create a secure connection to the SMTP server
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()

    mail_username = os.environ['MAIL_USERNAME']
    mail_password = os.environ['MAIL_PASSWORD']
    # Login to the email account
    server.login(mail_username, mail_password)

    # Send the email
    message = 'Subject: {}\n\n{}'.format(subject, message)
    server.sendmail(mail_username, recipient, message)

    server.quit()

# Get the sender and recipient email addresses from environment variables

recipient = os.environ['RECIPIENT_EMAIL']

# Get the subject and message from the script arguments
subject = 'Test email from GitHub Actions'
message = 'This is a test email sent from GitHub Actions.'

# Send the email
send_email(recipient, subject, message)
