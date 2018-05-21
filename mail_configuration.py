import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import config
import os
import time

path = "Unknown Person/"


def send_notifications():
    try:
        file = os.listdir(path)[0]
        email_user = config.EMAIL_ADDRESS
        email_password = config.PASSWORD
        email_send = config.EMAIL_ADDRESS
        subject = 'Unuthorized Person Detected!!'
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = 'This Mail Is Regarding Unknown Person Detected At College Premise. Kindly Take The Necessary Action.'
        msg.attach(MIMEText(body, 'plain'))
        filename = "Unknown Person/" + file
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()
        print('mail sent')
    except:
        print('no')

#send_notifications()
