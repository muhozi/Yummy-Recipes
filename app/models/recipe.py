from flask import session
from app.models.store import Store
from werkzeug.security import check_password_hash
import uuid
from datetime import datetime
from app.models.category import Category
class Recipe():
	"""Recipe Model"""
	name = None
	description = None
	category_id = None
	created = None
	owner_id = None
	def save(self, name,description,category_id):
		self.id = uuid.uuid4().hex
		self.name = name
		self.category_id = category_id
		self.description = description
		self.created = datetime.now()
		self.owner_id = session['user_id']
		data = {
			'id': self.id,
			'name': self.name,
			'category_id': self.category_id,
			'description': self.description,
			'owner_id': self.owner_id,
			'created_at': self.created
		}
		Store().save_recipe(data)
		return True

	def update(self, name,description,category_id,id):
		user_id = session['user_id']
		recipes = Store().get_user_recipes(user_id)
		for recipe in recipes:
			if self.is_exist(id):
				self.category_id = category_id
				self.name = name
				self.owner_id = recipe['owner_id']
				self.created = recipe['created_at']
				data = {
					'id': id,
					'category_id': self.category_id,
					'owner_id': self.owner_id,
					'name': name,
					'description': description,
					'created_at': self.created,
				}
				if (Store().update_recipe(data)):
					return True
				else:
					return False
			return True

	def delete(self, recipe_id):
		if (Store().delete_recipe(recipe_id)):
			return True
		else:
			return False
	def user_recipes(self):
		user_id = session['user_id']
		recipes = Store().get_user_recipes(user_id)
		for recipe in recipes:
			recipe['category'] = Category().category_name(recipe['category_id'])
		return recipes
	def recipe_exist(self,name):
		user_id = session['user_id']
		recipes = Store().get_user_recipes(user_id)
		for recipe in recipes:
			if (recipe['name'] == name):
				return True
		return False
	def exist_twice(self,name):
		user_id = session['user_id']
		recipes = Store().get_user_recipes(user_id)
		if (len(recipes) > 1):
			return True
		return False
	def is_exist(self,id):
		user_id = session['user_id']
		categories = Store().get_user_recipes(user_id)
		for category in categories:
			if (category['id'] == id):
				return True
		return False
		