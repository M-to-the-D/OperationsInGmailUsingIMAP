import imaplib
import email
from secret import *
emailID='abc@gmail.com'
username = un
password = pwd
mail_server = 'imap.gmail.com'
imap_server = imaplib.IMAP4_SSL(host=mail_server)
imap_server.login(username, password)
choice=0

while choice!=9:
    choice=int(input('1. Read email\n 2. list mailboxes\n 3. Create mailbox\n 4. Rename folder\n 5. Delete folder\n 6. Retrieve specific email\n  7. Delete an email\n 8. Clear all the mails\n 9. Exit\n Enter choice:'))

    # Find all emails in inbox and print out the raw email data    
    if choice==1:
        imap_server.select()
        _, message_numbers_raw = imap_server.search(None, 'ALL')
        for message_number in message_numbers_raw[0].split():
            _, msg = imap_server.fetch(message_number, '(RFC822)')
            print(msg[0][1])

    # List mailboxes
    elif choice==2:
        response_code, folders = imap_server.list()
        print(response_code)  
        print('Available folders(mailboxes) to select:')
        for folder_details_raw in folders:
            folder_details = folder_details_raw.decode().split()
            print(f'- {folder_details[-1]}')

    # Create mailboxes (folders)
    elif choice==3:
        response_code, response_details = imap_server.create('INBOX1.myfavorites')
        print(response_code)  
        print(response_details, ' Label Created!')
        
    #Rename folder
    elif choice==4:
        imap_server.rename('INBOX1.myfavorites', 'INBOX.faves')
        print('Renamed successfully')
    #Delete folder
    elif choice==5:
        imap_server.delete('INBOX.faves')
        print('Deleted successfully')
        #imap_server.select('INBOX')
   
    #Retrieve specific email
    elif choice==6:
        imap_server.select('INBOX')
        result, data = imap_server.search(None, '(FROM "cde@gmail.com" SUBJECT "test")' )
        ids = data[0] 
        id_list = ids.split() 
        latest_email_id = id_list[-1]
        result, data = imap_server.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        print(raw_email)
        
    #Delete an email
    elif choice==7:
        imap_server.select('INBOX')
        typ, data = imap_server.search(None, '(FROM "cde@gmail.com" SUBJECT "test")')
        for num in data[0].split():
            imap_server.store(num, '+FLAGS', r'(\Deleted)')
        imap_server.expunge()
        print("Mail Deleted")

    #clear all the mails
    elif choice==8:
        imap_server.select('Inbox')
        typ, data = imap_server.search(None, 'ALL')
        for num in data[0].split():
            imap_server.store(num, '+FLAGS', '\\Deleted')
            imap_server.expunge()
        
    #Exit
    elif choice==9:
        imap_server.close()
        imap_server.logout()

    
