from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=False)
    password= db.Column(db.String(80), unique=False)
    items = db.relationship('Item',backref='users',lazy='dynamic')
   
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
    thumbnail=db.Column(db.String(255))
    title = db.Column(db.String(80), unique=False)
    description= db.Column(db.String(80), unique=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
   
   
    def __init__(self, url, thumbnail, title, description,userid):
          self.url = url
          self.thumbnail = thumbnail
          self.title = title
          self.description = description 
          self.userid = userid
          
           
          