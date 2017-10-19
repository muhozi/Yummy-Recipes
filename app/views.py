from flask import render_template,session,redirect,flash,request,url_for,abort
from werkzeug.security import generate_password_hash
from datetime import datetime
from app import app
from app.forms import RegisterForm,LoginForm,RecipeForm,CategoryForm
from app.models.store import Store;
from app.models.user import User;
store = Store();
@app.route('/',methods=['POST','GET'])
def join():
	error=None
	print(store.get_users())
	form = RegisterForm.Register()
	if (request.method == 'GET'):
		return render_template("index.html",form = form)
	elif (request.method == 'POST'):
		if form.validate_on_submit():
			user = User(
				name=request.form['name'],
				email=request.form['email'],
				password=generate_password_hash(request.form['password']),
				created=datetime.now()
			)
			user.save()
			# User successfully registered
			return redirect(url_for('recipes'))
		error = form.errors
		flash(error,category='error')
		flash(request.form,category='input')
		return redirect(redirect_back())
	return abort(404)

@app.route('/login',methods = ['POST','GET'])
def login():
	if (request.method == 'GET'):
		form = LoginForm.Login()
		return render_template("login.html",form = form)
	elif (request.method == 'POST'):
		return "POST"
	return "OK"

@app.route('/addrecipe')
def addrecipe():
	users = store.get_users();
	print(users);
	form = RecipeForm.AddForm()
	return render_template("addrecipe.html",form=form)

def redirect_back(default='index'):
	return request.args.get('next') or \
		request.referrer or \
		url_for(default)
@app.route('/recipes')
def recipes():
	#Edit Recipe form details
	form = RecipeForm.EditForm()
	#Add form details
	#addCategory = CategoryForm.AddForm() # I ingnore it I will use JS
	#Add form details
	#category = CategoryForm.AddForm() # I ingnore it I will use JS
	return render_template("recipes.html",form=form)

