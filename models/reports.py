
from config import db
import datetime
from models.schedulertiming import TimingSchedule

class Reports(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    To = db.Column(db.String(255), nullable=True)
    From = db.Column(db.String(255), nullable=True)
    Bcc = db.Column(db.String(255), nullable=True)
    reportName = db.Column(db.String(255), nullable=True)
    folderName = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    reportCategoryID = db.Column(db.Integer, db.ForeignKey(
        'reportscategory.id'), nullable=True)
    schuduleTiming = db.relationship(
        "TimingSchedule", backref=db.backref("reports_scheduleTiming"))
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
