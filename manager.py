import os
from flask import Flask
from config import db, app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from models.reports import Reports
from models.mail_model import Mail
from models.schedulelog import ScheuleLog
from models.schedulertiming import TimingSchedule
from models.reportsCategory  import ReportsCategory
from models.notifications import Notifications


migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
