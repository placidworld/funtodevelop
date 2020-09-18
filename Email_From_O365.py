# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:43:10 2020

@author: heart
"""

 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os

from zipfile import ZipFile

 
credential_file = os.getenv('HOME') + '/.email_credential'

 
def get_email_credential():
       
    f = open(credential_file, "r")
    email_address = f.readline().strip()
    email_password = f.readline().strip()
    f.close()
   
    return [email_address, email_password]

 
def send_email(email_recipient, email_subject, email_message, attachment_file = None):
 
    try:
        [email_address, email_password] = get_email_credential()   
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_recipient
        msg['Subject'] = email_subject
       
        msg.attach(MIMEText(email_message, 'plain'))

        if attachment_file is not None:
            filename = os.path.basename(attachment_file)
            tmpfile = "/tmp/" + filename + ".zip"

           
            # zip the file
            with ZipFile(tmpfile, "w") as zipfile:
                zipfile.write(attachment_file, filename)

            with open(tmpfile, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s.zip" % filename)
                msg.attach(part)
                
            os.unlink(tmpfile)
            
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)

        text = msg.as_string()

        server.sendmail(email_address, email_recipient, text)

        server.quit()

        print('email sent')

    except:

        print("Failed to send mail.")

        return False

       
    return True



if __name__ == '__main__':

   
    # test the send_email function
    send_email('xxx@gmail.com',
           'Happy New Year',

           'We love Outlook',

           "/usr/bin/easy_install"

           )

#######
### Import this function and use as below:
    subject_line = ........
    send_email('xxx@gmail.com, xxx@yahoo.com',
               subject_line,
               'Dear xxx,\nPlease check file. \n\Emily)