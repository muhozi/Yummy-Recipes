import unittest
from datetime import datetime
import uuid
from app import app
from app.models.user import User
class FlaskClientTestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		self.client = app.test_client(use_cookies=True)
		self.single_user = {
			'id': uuid.uuid4().hex ,
			'name': 'Testing It',
			'email': 'test@tester.com',
			'password': 'secret',
			'repassword': 'secret'
        }
	def test_save_user(self):
		user = User(
			name=self.single_user['name'],
			email=self.single_user['email'],
			password=self.single_user['password'],
			created=datetime.now(),
			user_id=self.single_user['id'],
		)
		saved_user = user.save()
		self.assertTrue(saved_user)
	def tearDown(self):
		self.single_user = None
if __name__ == '__main__':
	unittest.main()