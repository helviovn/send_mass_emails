import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your email account credentials
email_address = '@gmail.pt'
email_password = 'password'

# List of recipients' email addresses
recipients = [
    '@gmail.com',
    # Add more recipients here
]

bcc_recipients = ['@gmail.com']

# List of specific codes for each recipient
codes = [
    'BE-2223-01TD-CTQJ',
    # Add more codes here
]

def get_ass():
     #assinatura
    ass = '''
       
    '''
    return ass


def send_email(to_email, subject, body,):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'PERSON'
    msg['To'] = to_email

    if bcc_recipients:
        msg['Bcc'] = ", ".join(bcc_recipients)

    signature = get_ass()
    body = body + signature
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    if bcc_recipients:
        recipients = [to_email] + bcc_recipients
    else:
        recipients = [to_email]
    server.sendmail(email_address, recipients, msg.as_string())
    server.quit()

subject = 'SUBJECT'


for recipient, code in zip(recipients, codes):
    body = f'BODY'
    send_email(recipient, subject, body)
    print(f'Email sent to {recipient} with code {code}')

print('All emails sent successfully.')