from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators
class Login(FlaskForm):
	"""Login Form"""
	email = StringField('email',[
		validators.DataRequired(message=u'Please enter your email'),
		validators.Email()
		])
	password = PasswordField('password',[
		validators.DataRequired(message=u'Please enter your password')
	])