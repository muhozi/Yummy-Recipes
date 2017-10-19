from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators
class Login(FlaskForm):
	"""Process Registration Form"""
	email = StringField('email',[
		validators.DataRequired(),
		validators.length(min=6,max=50)])
	password = PasswordField('password',[
		validators.DataRequired(),
	])