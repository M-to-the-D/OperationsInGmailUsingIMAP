from secret import *           #USER NAME AND PASSWORD IS IN secret.py
import smtplib
fromaddr = 'uchiha.md21@gmail.com'
toaddrs = input("Enter To address: ")#'uchiha.md21@gmail.com'
sub = input("Enter subject:  ")#"COMPUTER NETWORKS"
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
