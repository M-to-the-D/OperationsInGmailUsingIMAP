from secret import *           #USER NAME AND PASSWORD IS IN secret.py
import os
import smtplib
import imghdr
from email.message import EmailMessage

fromaddr = 'md@gmail.com'
username = un
password = pwd
targets = ['md@gmail.com', 'abc@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'TEST RUN'
msg['From'] = fromaddr
msg['To'] = ','.join(targets)
msg.set_content('SMTP')


msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>SMTP</title>
  </head>
  <body>
    <h1>SMTP</h1>
    <h3>SMTP is a set of communication guidelines that allow software to transmit an electronic mail over the internet is called Simple Mail Transfer Protocol.</h3>
    <h3>It provides a mail exchange between users on the same or different computers, and it also supports:</h3>
    <ul>
      <li>It can send a single message to one or more recipients.</li>
      <li>Sending message can include text, voice, video or graphics.</li>
      <li>It can also send the messages on networks outside the internet.</li>
    </ul>
  </body>
</html>
""", subtype='html')


with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(fromaddr,password)
    server.send_message(msg)
