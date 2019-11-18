from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

ma = Marshmallow(app)

app.config["SQLALCHEMY_ECHO"] = True
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://bhanu:bhanu123@localhost/sampleproject"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)


basedir = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
