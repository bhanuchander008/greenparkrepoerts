import os
import atexit
import sched
import time
import datetime
import schedule
from flask import Flask
from config import app
from flask_restful import Api
from flask_cors import CORS
from apscheduler.scheduler import Scheduler
from controllers.getpostschedular import Test, Users
from datetime import datetime, timedelta
from config import db
from flask import request
from flask import Flask, request
from threading import Thread
from mail import send_email
from os import path
from pathlib import Path
import json
app = Flask(__name__)
api = Api(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


home = str(Path.home())

i=1
alpha={}
with open('email.json') as f:
   obj = json.load(f)
   reportCategoryName=obj['data']["reportCategoryName"]
   mail_id=obj['data']["Tomails"]
   mail_id.append(str(i))
   Text=obj['data']['Text']
   Subject=obj['data']['subject']
   file_obj=obj['data']['fileName']
   alpha[tuple(mail_id)]=tuple(file_obj)
   i=i+1
print(alpha,".............../////////////")

def run_particular_hour():
    import subprocess
    from subprocess import Popen, PIPE
    print("starting")
    session = subprocess.Popen(
        ["tagui","D:/Tagui/Tagui_Icons/IDS_project.txt"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    out, err = session.communicate()
    print(out)
    # to = ["srinivas@hotelgreenpark.com","sivaprasad@hotelgreenpark.com","g.sivaprasad9@gmail.com","itmgr.hyd@marigoldhotels.com", "sumanth@caratred.com","rambabu@caratred.com","shashisridhar2@gmail.com"]
    # TEXT = "Hi This email from RPA"
    # SUBJECT = "Test Report"
    # send_email(to, ["flashreport1","flashreport2"],SUBJECT, TEXT)
    # print("endtime")
    TEXT = Text
    SUBJECT =Subject
    for emailid,textfiles in alpha.items():
       print(textfiles)
       send_email(emailid,("MG_FLASHREPORT.xls","MG_F&B_SUMMARY.xls"),SUBJECT,TEXT)

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


api.add_resource(Test, '/test')
api.add_resource(Users, '/user')

if __name__ == "__main__":
    schedule.every().day.at("07:00").do(run_particular_hour)
    t = Thread(target=run_schedule)
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
