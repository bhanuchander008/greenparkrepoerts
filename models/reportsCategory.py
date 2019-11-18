from config import db
import datetime
from models.reports import Reports

class ReportsCategory(db.Model):
    __tablename__ = "reportscategory"

    id             = db.Column(db.Integer, primary_key=True)
    departmentName = db.Column(db.String(255),nullable =True)
    status         = db.Column(db.String(255),nullable =True)
    reports        = db.relationship("Reports", backref = db.backref("reportscategory_report"))
    createdAt      = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updatedAt      = db.Column(db.DateTime, default = datetime.datetime.utcnow())
