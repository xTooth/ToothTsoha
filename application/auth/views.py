from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_login import login_required
from flask_bcrypt import Bcrypt

from application import app , db
from application.auth.models import User
from application.posts.models import Post
from application.auth.forms import LoginForm , NewUserForm

bcrypt = Bcrypt(app)

#login handler
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

#logout handler
@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#handles the list of current users on the platform
@app.route("/users", methods=["GET"])
def auth_users():
    return render_template("auth/list.html", users = User.query.all())


#sign up page handler
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

#handles the loading of a specific users page.
@app.route("/user/<user_id>",methods=["GET"])
def user_page(user_id):
    posts = Post.query.filter(Post.account_id == user_id).order_by(Post.date_modified.desc()).all()
    return render_template("auth/user.html", user = User.query.get(user_id), posts = posts)

#handles following of other users.
@app.route('/<user_id>/follow', methods=["POST"])
@login_required
def follow(user_id):
    user = User.query.get(user_id)
    current_user.add_follow(user)
    db.session.commit()
    return redirect(url_for("user_page", user_id= user_id))

#handles unfollowing of other users.
@app.route('/<user_id>/unfollow',methods=["POST"])
@login_required
def unfollow(user_id):
    user = User.query.get(user_id)
    current_user.unfollow(user)
    db.session.commit()
    return redirect(url_for('auth_users'))