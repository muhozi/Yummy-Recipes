from flask import Flask
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
app = Flask(__name__, instance_relative_config=True)
csrf.init_app(app)
# Load the views
from app import views

def create_app():
	return app
# Load the config file
app.config.from_object('config')