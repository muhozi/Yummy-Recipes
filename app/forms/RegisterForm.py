from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators
class Register(FlaskForm):
	"""Process Registration Form"""
	name = StringField('name',[
		validators.DataRequired(message=u'Enter your name'),
		validators.length(min=1,max=50)
	])
	email = StringField('email',[
		validators.DataRequired(message=u'Enter your email'),
		validators.Email(),
		validators.length(min=6,max=50)
	])
	password = PasswordField('password',[
		validators.DataRequired(message=u'Enter your password'),
		validators.EqualTo('repassword',message='Passwords do not match')
	])
	repassword = PasswordField('repassword',[
		validators.DataRequired(message=u'Confirm password'),
		validators.length(min=6,max=50)
	])