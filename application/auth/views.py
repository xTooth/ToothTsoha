from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required
from flask_bcrypt import Bcrypt

from application import app , db
from application.auth.models import User
from application.auth.forms import LoginForm , NewUserForm

bcrypt = Bcrypt(app)

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    pw = form.password.data
    user = User.query.filter_by(username=form.username.data).first()
    
    if not user:
         return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    if not bcrypt.check_password_hash(user.password, pw):
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    print("User " + user.name + " was identified")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/users", methods=["GET"])
def auth_users():
    return render_template("auth/list.html", users = User.query.all())



@app.route("/signup", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/signup.html", form = NewUserForm())

    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/signup.html" , form = form)
    
    pw = form.password.data
    pw_hash = bcrypt.generate_password_hash(pw).decode('utf-8')
    u = User(form.name.data, form.username.data , pw_hash)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))