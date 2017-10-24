from flask import session
from app.models.store import Store
from werkzeug.security import check_password_hash
import uuid
class Category(object):
	"""Category Model"""
	name = None
	category_id = None
	created = None
	owner_id = None
	def save(self, name,owner_id,created,category_id=None):
		self.name = name
		self.category_id = uuid.uuid4().hex
		self.created = created
		self.owner_id = owner_id
		data = {
			'id': self.category_id,
			'owner_id': owner_id,
			'name': self.name,
			'created_at': self.created,
		}
		if (self.category_exist(self.name)):
			return False
		Store().add_category(data)
		return True
	def user_categories(self):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		return categories

	def update(self, name,category_id):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		for category in categories:
			if self.is_exist(category_id):
				self.category_id = category_id
				self.name = name
				self.owner_id = category['owner_id']
				self.created = category['created_at']
				data = {
					'id': self.category_id,
					'owner_id': self.owner_id,
					'name': name,
					'created_at': self.created,
				}
				if (Store().update_category(data)):
					return True
				else:
					return False
			return True

	def delete(self, category_id):
		if (Store().delete_category(category_id)):
			return True
		else:
			return False

	def category_exist(self,name):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		for category in categories:
			if (category['name'] == name):
				return True
		return False
	def exist_twice(self,name):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		if (len(categories) > 1):
			return True
		return False
	def exist_categories(self):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		if (len(categories) > 0):
			return True
		return False
	def is_exist(self,id):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		for category in categories:
			if (category['id'] == id):
				return True
		return False
	def category_name(self,id):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		for category in categories:
			if (category['id'] == id):
				return category['name']
		