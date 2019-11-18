import os
import glob
import shutil
import smtplib
from os import path
from pathlib import Path
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from datetime import date, timedelta
#from  jsonrun import Json_obj
import json
import itertools
from pprint import pprint
yesterday = date.today() - timedelta(days=1)
date=yesterday.strftime('%d%m%y')


def send_email(emailid,textfiles,SUBJECT,TEXT):
   try:
       gmail_user = "bhanuchander008@gmail.com"
       gmail_pwd = 'sabhi1015'
       msg = MIMEMultipart()
       msg['From'] = gmail_user
       print(emailid,"before")
       emailid=list(emailid)
       emailid=[x for x in emailid if '.com' in x]
       print(emailid,"after")
       msg['To'] = ", ".join(emailid)
       msg['Subject'] = SUBJECT
       msg.attach(MIMEText(TEXT))
       home = str(Path.home())
       t="/Documents/fo/"
       my_path = home+t+date
    #    fpaths = [file for file in os.listdir(my_path)]
       #print("ospath",os.path)
       fpaths="C:\\Users\\ADMIN\\Documents\\fo\\260819\\"
       print(os.listdir(fpaths))
    #    print(">>>>>>>>>>>>>>>>>",fpaths)
       for y in textfiles:
           #print(y)
           if y in os.listdir(fpaths):
               print("filepaths",y)
               file_path = os.path.join(my_path, y)
               attachment = MIMEApplication(
                   open(file_path, "rb").read(), _subtype="txt")
               attachment.add_header(
                   'Content-Disposition', 'attachment', filename=y)
               msg.attach(attachment)
       mailServer = smtplib.SMTP("smtp.gmail.com:587")
       mailServer.ehlo()
       mailServer.starttls()
       mailServer.ehlo()
       mailServer.login(gmail_user, gmail_pwd)
       mailServer.sendmail(gmail_user, emailid, msg.as_string())
       mailServer.close()
       print('successfully sent the mail')
           # for f in fpaths:
           #     home = str(Path.home())
           #     destination = home+"/Downloads/test"+date
           #     shutil.move(path.join(my_path, f), destination)
           #     print("files are moved successfully")
   except Exception as e:
       print(str(e))
# # if __name__ == '__main__':
# TEXT = Text
# SUBJECT =Subject
# for emailid,textfiles in alpha.items():
#    print(textfiles)
#    send_email(emailid,textfiles,SUBJECT,TEXT)