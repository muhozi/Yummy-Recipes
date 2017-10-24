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
		Update Recipe
	"""
	def update_recipe(self,data):
		for recipe in self.recipes:
			if recipe['id'] == data['id']:
				recipe['name'] = data['name']
				recipe['category_id'] = data['category_id']
				recipe['description'] = data['description']
				return True
		return False

	"""
		Delete Category and Its Recipes
	"""
	def delete_category(self,id):
		incr = 0
		recipe_incr = 0
		for category in self.categories:
			if category['id'] == id:
				for recipe in self.recipes:
					if (recipe['category_id'] == id):
						del self.recipes[recipe_incr]
					recipe_incr+1
				del self.categories[incr]
				return True
			incr+1
		return False
	"""
		Delete Recipe
	"""
	def delete_recipe(self,id):
		incr = 0
		for recipe in self.recipes:
			if recipe['id'] == id:
				del self.recipes[incr]
				return True
			incr+1
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
		Get user categories
	"""
	def get_user_recipes(self,user_id):
		user_recipes = []
		for recipe in self.recipes:
			if recipe['owner_id'] == user_id:
				user_recipes.append(recipe)
		return user_recipes
	
	"""
		Empty Store
	"""
	def clear(self,data):
		self.users=[]