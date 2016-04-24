from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, FileField, SubmitField
from wtforms.validators import Required, url
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import PasswordField, validators
from wtforms.fields.html5 import URLField

class LoginForm(Form):
   
    email = TextField('Email', validators=[Required()])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')
    submit = SubmitField('Submit')

    
class Additem(Form):
   url = URLField(validators=[url()])
   thumbnail=FileField('Image')
   title = TextField('title', validators=[Required()])
   description= TextAreaField('description', validators=[Required()])
   
class Register(Form):
<<<<<<< HEAD
    username = TextField('Username', validators=[Required()])
    email = TextField('Email', [validators.Length(min=6, max=35)])
=======
    username = TextField('Firstname', validators=[Required()])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
>>>>>>> 8567172ac758c6e4e965c4440b775be693c3eba0
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')
    submit = SubmitField("Submit")
   
   
