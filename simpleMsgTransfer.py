from secret import *           #USER NAME AND PASSWORD IS IN secret.py
import smtplib
fromaddr = 'md@gmail.com'
toaddrs = input("Enter To address: ")
sub = input("Enter subject:  ")
body=input("Enter body: ")#'Hello! Test run successfully done.'
username = un
password = pwd
server = smtplib.SMTP_SSL('smtp.gmail.com')#GMAIL
#server.ehlo()
#server.starttls()
#server.ehlo()

server.login(fromaddr,password)

msg=f'Subject: {sub}\n\n{body}'
server.sendmail(fromaddr, toaddrs, msg)
print("Email sent successfully")
#server.quit()
