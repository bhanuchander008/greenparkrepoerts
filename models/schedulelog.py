from config import db
import datetime


class ScheuleLog(db.Model):
    __tablename__ = "schedulelog"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=True)
    time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
