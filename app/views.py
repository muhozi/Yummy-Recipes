from flask import render_template,session,redirect,flash,request,url_for
from app import app
from app.forms import RegisterForm,LoginForm,RecipeForm,CategoryForm
@app.route('/')
def index():
	form = RegisterForm.Register()
	return render_template("index.html",form = form)

@app.route('/login')
def login():
	form = LoginForm.Login()
	return render_template("login.html",form = form)

@app.route('/addrecipe')
def addrecipe():
	form = RecipeForm.AddForm()
	return render_template("addrecipe.html",form=form)

@app.route('/recipes')
def recipes():
	#Edit Recipe form details
	form = RecipeForm.EditForm()
	#Add form details
	#addCategory = CategoryForm.AddForm() # I ingnore it I will use JS
	#Add form details
	#category = CategoryForm.AddForm() # I ingnore it I will use JS
	return render_template("recipes.html",form=form)

@app.route('/join',methods=['POST'])
def join():
	form = RegisterForm.Register(request.form)
	if form.validate():
		print('OK')
		flash('You have successfully registered','message')
	else:
		print("Error")
	return redirect('/',errors = errors)

