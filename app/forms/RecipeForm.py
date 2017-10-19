from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators, SelectField
class AddForm(FlaskForm):
	""" Add Recipe Form"""
	name = StringField('name',[
		validators.DataRequired(),
		validators.length(min=3,max=50)
	])
	category = SelectField(u'Programming Language', choices=[('burgers','Burgers'),('Chicken','Chicken'),('Pizza','Pizza')])
	description = TextAreaField('description',[
		validators.DataRequired(),
		validators.length(min=6,max=500)
	])


class EditForm(FlaskForm):
	"""Edit Recipe Form"""
	name = StringField('name',[
		validators.DataRequired(),
		validators.length(min=3,max=50)
	])
	category = SelectField(u'Programming Language', choices=[('burgers','Burgers'),('Chicken','Chicken'),('Pizza','Pizza')])
	description = TextAreaField('description',[
		validators.DataRequired(),
		validators.length(min=6,max=500)
	])