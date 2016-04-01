from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField
from wtforms.validators import Required, url
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import PasswordField, validators
from wtforms.fields.html5 import URLField

class LoginForm(Form):
   
    username = TextField('Firstname', validators=[Required()])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')
    
class Additem(Form):
   url = URLField(validators=[url()])
   title = TextField('title', validators=[Required()])
   description= TextAreaField('description', validators=[Required()])
   
   
   
   
