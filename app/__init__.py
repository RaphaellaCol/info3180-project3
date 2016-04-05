from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project3:info3180@localhost/project3db'
db = SQLAlchemy(app)
from models import *

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zacldghmaphilm:J_Fqd12eogbaJfUAdhROB33nGz@ec2-107-20-222-114.compute-1.amazonaws.com:5432/ddkadcpjqh4jtn'
#db.drop_all()
db.create_all()

db.session.commit()
from app import views, models