#!/bin/bash/python3
import smtplib
from email.mine.multipart import MIMEMultipart
from email.mine.text import MIMEText
mail_content = '''
Testing Failed.
'''
#The mail addresses and password
sender_address = 'test@gmail.com'
sender_pass = 'zyz'
receiver_address = 'dev@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Testing status'   # The subject line
#the body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com',587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text=message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
