class Store():
	"""Store class"""
	users = []
	recipes = []
	categories = []
	def __init__(self):
		super(Store, self).__init__()

	"""
		Store user
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
		Store new category
	"""
	def add_category(self,user_id,data):
		categories = self.get_user_categories(user_id)
		categories.append(data)

	"""
		Get user categories
	"""
	def get_user_categories(self,user_id):
		for single_user in self.users:
			if single_user['id'] == user_id:
				return single_user['categories']

	"""
		Empty Store
	"""
	def clear(self,data):
		self.users=[]