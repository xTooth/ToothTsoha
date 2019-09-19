from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required
from flask_bcrypt import bcrypt

from application import app , db
from application.auth.models import User
from application.auth.forms import LoginForm , NewUserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
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

@app.route("/signup", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/signup.html", form = NewUserForm())

    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/signup.html" , form = form)

    u = User(form.name.data, form.username.data , form.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))