
from config import db
import datetime


class Notifications(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    mobileNumbers = db.Column(db.String(100), nullable=True)
    emails = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
