from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project3db'
db = SQLAlchemy(app)
from models import *


#db.drop_all()
db.create_all()

db.session.commit()
from app import views, models