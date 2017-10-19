from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators
class AddForm(FlaskForm):
	"""Process Registration Form"""
	name = StringField('name',[validators.length(min=3,max=50)])