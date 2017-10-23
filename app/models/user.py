from app.models.store import Store
from werkzeug.security import check_password_hash
import uuid
class User(object):
	"""User Model"""
	name = None
	email = None
	password = None
	user_id = None
	created = None
	def save(self, name, email, password, created, user_id=None):
		self.name = name
		self.email = email
		self.password = password
		self.user_id = uuid.uuid4().hex if user_id is None else user_id
		self.created = created
		data = {
			'id': self.user_id,
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'created_at': self.created,
			'categories': list(),
		}
		if (self.email_exist(self.email)):
			return False
		Store().add_user(data)
		return True
	def email_exist(self,email):
		users = Store().get_users()
		for user in users:
			if (user['email'] == email):
				return True
		return False
	def exist(self,email,password):
		users = Store().get_users()
		for user in users:
			# print(check_password_hash(user['password'], password))
			if (user['email'] == email and check_password_hash(user['password'], password)):
				self.user_id = user['id']
				self.name = user['name']
				self.email = user['email']
				self.password = user['password']
				return True
		return False
		