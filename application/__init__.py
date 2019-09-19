# flask & bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

# database
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# application
from application import views

from application.posts import models
from application.posts import views

from application.auth import models
from application.auth import views

# logins
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# create tables
db.create_all()