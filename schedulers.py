# import datetime
# import schedule
# import time
# import subprocess
# from subprocess import Popen, PIPE
# from flask import Flask
#
# app = Flask(__name__)
#
#
# def test():
#     print("starting")
#     session = subprocess.Popen(
#         ["sh", "./run.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     out, err = session.communicate()
#     print(out)
#     print("endtime")
#
# schedule.every(10).seconds.do(test)
# schedule.every().day.at("15:16").do(test)
# while True:
#    schedule.run_pending()
#    time.sleep(1)
#
#
#
#  #
#  sched = Scheduler(daemon=True)
#  sched.start()
#
#  # @sched.interval_schedule(hours=10)
#  # def test():
#  #     import subprocess
#  #     from subprocess import Popen, PIPE
#  #     print("starting")
#  #     session = subprocess.Popen(
#  #         ["sh", "./run.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#  #     out, err = session.communicate()
#  #     print(out)
#  #     print("endtime")
#  # atexit.register(lambda: sched.shutdown(wait=False))
#  #
#
#  #api.add_resource(GetcreateScheduler, '/postscheduler')
