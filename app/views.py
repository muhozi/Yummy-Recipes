from flask import render_template,session,redirect,flash,request,url_for,abort
from functools import wraps
from werkzeug.security import generate_password_hash
from datetime import datetime
from app import app
from app.forms import RegisterForm,LoginForm,RecipeForm,CategoryForm
from app.models.store import Store;
from app.models.user import User;
store = Store();

""" 
	Only logged in user Middleware function
"""
def auth(n):
	@wraps(n)
	def wrap(*args, **kwargs):
		if 'logged_in' in session and session['logged_in'] == True:
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
				session['id'] = user.user_id
				session['name'] = user.name
				session['email'] = user.email
				flash('Thanks for joining us',category='successMessage')
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
				session['id'] = user.user_id
				session['name'] = user.name
				session['email'] = user.email
				flash('welcome back to Yummy recipes community',category='successMessage')
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
	Redirect back
"""
def redirect_back(default='join'):
	return request.args.get('next') or \
		request.referrer or \
		url_for(default)

"""
	Recipes route
"""
@app.route('/recipes')
@auth
def recipes():
	form = RecipeForm.EditForm() #Edit Recipe form
	addCategory = CategoryForm.AddForm() #Addcategory  form
	return render_template("recipes.html",form=form,categoryForm = addCategory)

