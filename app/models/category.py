from flask import session
from app.models.store import Store
from werkzeug.security import check_password_hash
import uuid
class Category(object):
	"""User Model"""
	name = None
	category_id = None
	created = None
	def save(self, name, created, category_id=None):
		self.name = name
		self.category_id = uuid.uuid4().hex
		self.created = created
		data = {
			'id': self.category_id,
			'name': self.name,
			'created_at': self.created,
			'recipes': [],
		}
		if (self.category_exist(self.name)):
			return False
		Store().add_category(session['user_id'],data)
		return True
	def category_exist(self,name):
		user_id = session['user_id']
		categories = Store().get_user_categories(user_id)
		for user in categories:
			if (user['name'] == name):
				return True
		return False
	# def exist(self,email,password):
	# 	users = Store().get_users()
	# 	for user in users:
	# 		# print(check_password_hash(user['password'], password))
	# 		if (user['email'] == email and check_password_hash(user['password'], password)):
	# 			self.user_id = user['id']
	# 			self.name = user['name']
	# 			self.email = user['email']
	# 			self.password = user['password']
	# 			return True
	# 	return False
		