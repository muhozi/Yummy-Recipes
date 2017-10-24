from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, validators, SelectField
from app.models.store import Store
""" Add Recipe Form"""
def addRecipe(categories_list):
	class AddForm(FlaskForm):
		name = StringField('name',[
			validators.DataRequired(message="What is the name of recipe?"),
			validators.length(min=3,max=50)
		])
		category = SelectField(u'Recipes', choices=categories_list)
		description = TextAreaField('description',[
			validators.DataRequired(message="Describe the recipe please"),
			validators.length(min=6,max=500,message=u'Please enter meaningful description')
		])
	return AddForm()
def editRecipe(categories_list):
	class EditForm(FlaskForm):
		"""Edit Recipe Form"""
		name = StringField('name',[
			validators.DataRequired(),
			validators.length(min=3,max=50)
		])
		category = SelectField(u'Recipes', choices=categories_list)
		description = TextAreaField('description',[
			validators.DataRequired(),
			validators.length(min=6,max=500)
		])
	return EditForm()