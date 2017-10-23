class Store():
	"""Store class"""
	users = []
	recipes = []
	categories = []
	def __init__(self):
		super(Store, self).__init__()

	"""
		Add user
	"""
	def add_user(self,data):
		self.users.append(data)
	
	def save_recipe(self,data):
		self.recipes.append(data)
	def save_category(self,data):
		self.categories.append(data)

	"""
		Get all users
	"""
	def get_users(self):
		return self.users

	"""
		Empty Store
	"""
	def clear(self,data):
		self.users=[]