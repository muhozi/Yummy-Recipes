from flask import render_template,session,redirect,flash,request,url_for,abort
from functools import wraps
from werkzeug.security import generate_password_hash
from datetime import datetime
from app import app
from app.forms import RegisterForm,LoginForm,RecipeForm,CategoryForm
from app.models.store import Store;
from app.models.user import User;
from app.models.category import Category;
# Remove this before pushing
import uuid
store = Store();
""" 
	Only logged in user Middleware function
"""
def auth(n):
	@wraps(n)
	def wrap(*args, **kwargs):
		if 'logged_in' in session and session['logged_in'] == True and 'user_id' in session and session['logged_in']:
			return n(*args, **kwargs)
		else:
			return redirect(url_for('login'))
	return wrap

""" 
	Only Guest user Middleware function
"""
def guest(n):
	@wraps(n)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return redirect(url_for('recipes'))
		else:
			return n(*args, **kwargs)

	return wrap

"""
	Registration route | Index route
"""
@app.route('/',methods=['POST','GET'])
@guest
def join():
	error=None
	form = RegisterForm.Register()
	if (request.method == 'GET'):
		return render_template("index.html",form = form)
	elif (request.method == 'POST'):
		if form.validate_on_submit():
			user = User()
			user_saved = user.save(
				name=request.form['name'],
				email=request.form['email'],
				password=generate_password_hash(request.form['password']),
				created=datetime.now()
			)
			if ( user_saved ):
				session['logged_in'] = True
				session['user_id'] = user.user_id
				session['name'] = user.name
				session['email'] = user.email
				flash(session["name"]+ ' Thanks for joining us',category='successMessage')
				return redirect(url_for('recipes'))
			flash('Email already exists',category='errorMessage')
			flash(request.form,category='input')
			return redirect(redirect_back())
		error = form.errors
		flash(error,category='error')
		flash(request.form,category='input')
		return redirect(redirect_back())
	return abort(404)

"""
	Login route
"""
@app.route('/login',methods = ['POST','GET'])
@guest
def login():
	error = None
	form = LoginForm.Login()
	if (request.method == 'GET'):
		return render_template("login.html",form = form)
	elif (request.method == 'POST'):
		if form.validate_on_submit():
			user = User()
			user_exist = user.exist(request.form['email'],request.form['password'])
			if ( user_exist ):
				session['logged_in'] = True
				session['user_id'] = user.user_id
				session['name'] = user.name
				session['email'] = user.email
				flash(session["name"]+ ' welcome back to Yummy recipes community',category='successMessage')
				return redirect(url_for('recipes'))
			flash('Invalid email or password',category='errorMessage')
			flash(request.form,category='input')
			return redirect(redirect_back())
		error = form.errors
		flash(error,category='error')
		flash(request.form,category='input')
		return redirect(redirect_back())
	return abort(404)

"""
	Logout route
"""
@app.route('/logout')
@auth
def logout():
	session.clear()
	return redirect(url_for('login'))

"""
	Add Recipe route
"""
@app.route('/addrecipe')
@auth
def addrecipe():
	users = store.get_users();
	form = RecipeForm.AddForm()
	return render_template("addrecipe.html",form=form)

"""
	Recipes route
"""
@app.route('/recipes')
@auth
def recipes():
	form = RecipeForm.EditForm() #Edit Recipe form
	addCategory = CategoryForm.AddForm() #Addcategory  form
	categories = Store().get_user_categories(session['user_id'])
	return render_template("recipes.html",form=form,categoryForm = addCategory,categories=categories)


"""
	Recipes route
"""
@app.route('/addcategory',methods=['POST'])
@auth
def add_category():
	form = CategoryForm.AddForm()
	if form.validate_on_submit():
		category = Category()
		if category.category_exist(request.form['name']):
			flash('This category already exists',category='errorMessage')
			return redirect(redirect_back())
		save_category = category.save(
			owner_id = session['user_id'],
			name = request.form['name'],
			created = datetime.now())
		if ( save_category ):
			flash(' Category \'{0}\' has been successfully saved'.format(category.name),category='successMessage')
			return redirect(redirect_back())
		flash('Unable to save category',category='errorMessage')
		flash(request.form,category='input')
		return redirect(redirect_back())
	error = form.errors
	flash(error,category='error')
	flash(request.form,category='input')
	return redirect(redirect_back())

""" 
	Edit Category route
"""
@app.route('/editcategory/<id>',methods=['POST'])
@auth
def edit_category(id):

	form = CategoryForm.AddForm()
	if form.validate_on_submit():
		category = Category()
		if (category.is_exist(id) != True):
			flash('Sorry,That category doesn\'t exist',category='errorMessage')
			return redirect(redirect_back())
		if category.exist_twice(request.form['name']):
			flash('Sorry,There is another category with the same name',category='errorMessage')
			return redirect(redirect_back())
		save_category = category.update(request.form['name'],id)
		if ( save_category ):
			flash(' Category \'{0}\' has been successfully updated'.format(category.name),category='successMessage')
			return redirect(redirect_back())
		flash('Unable to save category',category='errorMessage')
		flash(request.form,category='input')
		return redirect(redirect_back())
	error = form.errors
	flash(error,category='error')
	flash(request.form,category='input')
	return redirect(redirect_back())

""" 
	Delete Category route
"""
@app.route('/deletecategory/<id>',methods=['GET'])
@auth
def delete_category(id):
	category = Category()
	if (category.is_exist(id) != True):
		flash('Sorry,That category doesn\'t exist',category='errorMessage')
		return redirect(redirect_back())
	delete_category = category.delete(id)
	if ( delete_category ):
		flash(' Category has been successfully deleted',category='successMessage')
		return redirect(redirect_back())
	flash('Unable to save category',category='errorMessage')
	flash(request.form,category='input')
	return redirect(redirect_back())

""" 
	Redirect back
"""
def redirect_back(default='join'):
	return request.args.get('next') or \
		request.referrer or \
		url_for(default)

