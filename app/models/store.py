class Store():
	"""Store class"""
	users = []
	recipes = []
	categories = []
	def __init__(self, arg=None):
		super(Store, self).__init__()
		self.arg = arg
	def add_user(self,data):
		self.users.append(data)
	def save_recipe(self,data):
		self.recipes.append(data)
	def save_category(self,data):
		self.categories.append(data)
	def get_users(self):
		return self.users