from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField
from wtforms.validators import Required, Email, EqualTo
import menuParser
class RegisterForm(Form):
	username = TextField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	confirm = PasswordField('Password', validators=[Required(), EqualTo('password', 'Passwords do not match.')])
	firstFoods = SelectMultipleField('Which meals are your favorites? (Choose 5)',validators=[],
		choices=[(str(item),str(item)) for item in menuParser.allMeals()])
	secondFoods = SelectMultipleField('Which meals are your second favorites? (Choose 5)',validators=[],
		choices=[(str(item),str(item)) for item in menuParser.allMeals()])
	thirdFoods = SelectMultipleField('Which meals are your third favorites? (Choose 5)',validators=[],
		choices=[(str(item),str(item)) for item in menuParser.allMeals()])


class LoginForm(Form):
	username = TextField('Userame', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])