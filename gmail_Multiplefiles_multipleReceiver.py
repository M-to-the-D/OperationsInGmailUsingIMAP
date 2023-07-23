from secret import *           #USER NAME AND PASSWORD IS IN secret.py
import smtplib
from email.message import EmailMessage
import imghdr
import shutil, os
fromaddr = 'uchiha.md21@gmail.com'
#toaddrs = 'uchiha.md21@gmail.com'
username = un
password = pwd
targets = ['uchiha.md21@gmail.com', 'dhikshita.m@gmail.com', 'bashidshaneilhussain@gmail.com']

msg=EmailMessage()
msg['Subject'] = 'COMPUTER NETWORKS'
msg['From'] = fromaddr
msg['To'] = ','.join(targets)
msg.set_content('Welcome to Sastra University..')

files=['SASTRA.jpg', 'Sastra2.jpeg', 'softSkillsSpeech.pdf', 'Eduminatti.docx']

for i in files:
    fileName,fileExtension = os.path.splitext(i)
    with open(i, 'rb') as f:
        file_type= str(imghdr.what(f.name))
        if fileExtension is None:
            mt='application'
            file_type='octet-stream'
        if fileExtension == '.docx':
            mt='text'
        elif fileExtension in ['.jpg', '.png', '.jpeg']:
            mt='image'
        elif fileExtension is '.pdf':
            mt='application'
            file_type='octet-stream'
        elif fileExtension == '.mp3':
            mt='audio'
        elif fileExtension == '.mp4':
            mt='video'
            
        msg.add_attachment(f.read(), maintype=mt, subtype=file_type, filename=f.name)

with smtplib.SMTP('smtp.gmail.com',587) as server:#GMAIL
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr,password)
    server.send_message(msg)
    #server.sendmail(fromaddr, toaddrs, msg)

#server.quit()
