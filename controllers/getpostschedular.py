import os
from datetime import datetime
from flask import make_response,abort,request
from models.schedulertiming import TimingSchedule
from config import db
from flask_restful import reqparse, abort, Api, Resource
from config import db,basedir
import logging, logging.config, yaml
from datetime import date, timedelta
from os import path
from pathlib import Path

home = str(Path.home())

folder = "/Documents/fo"
yesterday = date.today() - timedelta(days=1)
date=yesterday.strftime('%d%m%y')
path = home+folder+"/"+date

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)


class Test(Resource):
    def __init__(self):
        pass
    def get(self):
                from datetime import date, timedelta
                yesterday = date.today() - timedelta(days=1)
                date=yesterday.strftime('%d%m%y')
                reportname ="falshreport"
                base_dir = home+"/Documents/fo"
                d=os.path.join(base_dir,date)
                dict = [{"reportName":"flashreport","fileName":"MG_FLASHREPORT.xls", "folderName":d,
                       "reportDate":date,"Form_number":"fomr650","reportId":10},
                       {"reportName":"flashreport","fileName":"MG_F&B_SUMMARY.xls", "folderName":d,
                               "reportDate":date,"formNum":"fomr650","reportId":14}]

                return({"success":True,"Report":dict})


class Users(Resource):
    def __init__(self):
        pass
    def get(self):
        dict ={"userName":"RPAREPORTS","Password":"RPA@2019"}
        return({"success":True,"data":dict})










#
# CONFIG_PATH = os.path.join(basedir,'loggeryaml/schedulertiming.yaml')
# logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
# logger = logging.getLogger('postschedulers')
# loggers = logging.getLogger("consoleschedulers")

# class GetcreateScheduler(Resource):
#     def __init__(self):
#         pass
#     def get(self):
#         try:
#             schedule_obj=db.session.query(TimingSchedule).order_by(TimingSchedule.id).all()
#             print(schedule_obj)
#             if schedule_obj:
#                 schedule_schema = TimingScheduleSchema(many=True)
#                 data = schedule_schema.dump(schedule_obj).data
#                 logger.info("data feteched successfully")
#                 loggers.info("data feteched successfully")
#                 return({"success":True,"data":data})
#             else:
#                 logger.warning("scheduler not found")
#                 loggers.warning("roles not found")
#                 return({"success":False,"message": "scheduler not found"})
#         except Exception as e:
#             logger.warning(str(e))
#             loggers.warning(str(e))
#             return({"success":False,"message":str(e)})
#
#
#     def post(self):
#         try:
#             da = request.get_json()
#             schedule_schema = TimingScheduleSchema()
#             schema_obj= schedule_schema.load(da, session=db.session).data
#             db.session.add(schema_obj)
#             db.session.commit()
#             data = schedule_schema.dump(schema_obj).data
#             logger.info("data posted successfully")
#             loggers.info("data posted successfully")
#             return({"success":True,"data":data})
#         except Exception as e:
#             logger.warning(str(e))
#             loggers.warning(str(e))
#             return({"success":False,"message":str(e)})
