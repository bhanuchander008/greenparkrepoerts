from config import db
import datetime
from flask_sqlalchemy import SQLAlchemy


class TimingSchedule(db.Model):
    __tablename__ = 'timingschedule'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=True)
    reportId = db.Column(db.Integer, db.ForeignKey(
        'reports.id'), nullable=True)
    seconds = db.Column(db.String(100), nullable=True)
    minutes = db.Column(db.String(100), nullable=True)
    hours = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
