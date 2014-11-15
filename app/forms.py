from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField
from wtforms.validators import Required, Email, EqualTo

class RegisterForm(Form):
	teamname = TextField('Team Name', validators=[Required()])
	names = TextField('Names', validators=[Required()])
	languages = SelectMultipleField('Languages', validators=[], 
		choices=[('python', 'Python'), ('java','Java'),('javascript','Javascript')])
	email = TextField('Email', validators=[Required(), Email()])
	password = PasswordField('Password', validators=[Required()])
	confirm = PasswordField('Password', validators=[Required(), EqualTo('password', 'Passwords do not match.')])

class LoginForm(Form):
	teamname = TextField('Team Name', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])