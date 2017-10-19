from app.models.store import Store
import uuid
class User(object):
	"""User Model"""
	def __init__(self, name, email, password, created, user_id=None,):
		self.name = name
		self.email = email
		self.password = password
		self.user_id = uuid.uuid4().hex if user_id is None else user_id
		self.created = created
	def save(self):
		data = {
			'id': self.user_id,
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'created_at': self.created,
		}
		Store().add_user(data)
		return True
		