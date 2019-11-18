from config import db
import datetime
from flask_sqlalchemy import SQLAlchemy


class Mail(db.Model):
    __tablename__ = 'mail'

    id = db.Column(db.Integer, primary_key=True)
    reportName = db.Column(db.String(100), nullable=True)
    fileName = db.Column(db.String(100), nullable=True)
    formDate = db.Column(db.String(100), nullable=True)
    fomrNumber = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
