class Store():
	"""docstring for Store"""
	def __init__(self, arg):
		super(Store, self).__init__()
		self.arg = arg
		users = [];
		recipes = [];
		categories = [];
	def save_user(self,data):
		self.users.append(data);
	def save_recipe(self,data):
		self.recipes.append(data)
	def save_category(self,data):
		self.categories.append(data);