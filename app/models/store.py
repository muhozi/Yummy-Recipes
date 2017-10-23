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
		Add new category
	"""
	def add_category(self,data):
		self.categories.append(data)
	"""
		Edit Category
	"""
	def update_category(self,data):
		for category in self.categories:
			if category['id'] == data['id']:
				category['name'] = data['name']
				return True
		return False

	"""
		Edit Category
	"""
	def delete_category(self,id):
		incr = 0
		for category in self.categories:
			if category['id'] == id:
				del self.categories[incr]
				incr+1
				return True
		return False

	"""
		Get user categories
	"""
	def get_user_categories(self,user_id):
		user_categories = []
		for category in self.categories:
			if category['owner_id'] == user_id:
				user_categories.append(category)
		return user_categories

	"""
		Empty Store
	"""
	def clear(self,data):
		self.users=[]