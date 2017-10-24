import unittest
from datetime import datetime
import uuid
from urllib.parse import urlparse
from app import app
from app.models.user import User
from werkzeug.security import generate_password_hash
class FlaskClientTestCase(unittest.TestCase):

	def setUp(self):
		""" 
			Set up tet data
		"""	
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
		self.exist_user = {
			'id': uuid.uuid4().hex ,
			'name': 'Andelan',
			'email': 'andelan@andela.com',
			'password': 'secret',
			'repassword': 'secret'
		}
		user = User().save(
			name=self.exist_user['name'],
			email=self.exist_user['email'],
			password=generate_password_hash(self.exist_user['password']),
			created=datetime.now(),
			user_id=self.exist_user['id'],
		)

	def test_register(self):
		""" 
			Test Registration
		"""
		response = self.client.post('/', data=dict(
			name=self.single_user['name'],
			email=self.single_user['email'],
			password=self.single_user['password'],
			repassword=self.single_user['repassword']),
			follow_redirects=True
		)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Thanks for joining us', response.data)

	def test_logout(self):
		""" 
			Test Logout
		"""
		response = self.client.get('/logout')
		self.assertEqual(response.status_code, 302)
		self.assertEqual(urlparse(response.location).path, '/login')

	def test_login(self):
		""" 
			Test Login
		"""
		response = self.client.post('/login', data=dict(
			email=self.exist_user['email'],
			password=self.exist_user['password']),
			follow_redirects=True
		)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'welcome back', response.data)

	def tearDown(self):
		""" 
			Destroy tests data
		"""
		self.single_user = None
		self.exist_user = None
if __name__ == '__main__':
	unittest.main()