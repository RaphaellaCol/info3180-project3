from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=False)
    password= db.Column(db.String(80), unique=False)
   
    def __init__(self, username, email, password):
          self.username = username
          self.email = email
          self.password = password

def __repr__(self):
        return '<User %r>' % self.username
        
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=False)
    title = db.Column(db.String(80), unique=False)
    description= db.Column(db.String(80), unique=False)
   
   
    def __init__(self, url, title, description):
          self.url = url
          self.title = title
          self.description = description 
          
           
          