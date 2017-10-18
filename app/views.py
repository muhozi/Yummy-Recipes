from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")